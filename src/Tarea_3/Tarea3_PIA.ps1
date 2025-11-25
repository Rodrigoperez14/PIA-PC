#! /bin/pwsh

param([string]$accion = "default")

Set-StrictMode -Version Latest

function Procesos_Activos {
    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $archivo = "Procesos_activos_$timestamp"
    $csvPath = "$env:USERPROFILE/Desktop/$archivo.csv"
    $jsonlLog = "$env:USERPROFILE/Desktop/Logs.jsonl"

    Get-Process | Select-Object Name, Id, Path | Export-Csv -Path $csvPath -NoTypeInformation

    $logEntry = [PSCustomObject]@{
        timestamp = (Get-Date).ToString("s")
        task      = "Procesos_Activos"
        status    = "OK"
        output    = $csvPath
    }
    $logEntry | ConvertTo-Json -Compress | Out-File -FilePath $jsonlLog -Append -Encoding utf8

    Write-Host "✅ Procesos exportados a: $csvPath"
}

function Conexion_Internet {
    param([string]$archivo = "Conexiones_Procesos")

    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $archivo = "${archivo}_$timestamp"
    $csvPath = "$env:USERPROFILE/Desktop/$archivo.csv"
    $jsonlLog = "$env:USERPROFILE/Desktop/Logs.jsonl"

    $listaIP = @()
    $Conexion = Get-NetTCPConnection | Where-Object { $_.State -in @("Established","Listen") }
    $Procesos = Get-CimInstance Win32_Process | Select-Object ProcessId, Name, ExecutablePath

    $datos = @()

    foreach ($conn in $Conexion) {
        $Id = $conn.OwningProcess
        $tarea = $Procesos | Where-Object { $_.ProcessId -eq $Id }
        $estadoFirma = $null
        if ($tarea -and $tarea.ExecutablePath) {
            $firma = Get-AuthenticodeSignature -FilePath $tarea.ExecutablePath
            $estadoFirma = $firma.Status
        }

        $datos += [PSCustomObject]@{
            Firma         = $estadoFirma
            Estado        = $conn.State
            LocalAddress  = $conn.LocalAddress
            LocalPort     = $conn.LocalPort
            RemoteAddress = $conn.RemoteAddress
            RemotePort    = $conn.RemotePort
            PID           = $Id
            Proceso       = $tarea.Name
            Ruta          = $tarea.ExecutablePath
        }

        if ($conn.RemoteAddress -notin @("0.0.0.0","127.0.0.1","::")) {
            $listaIP += $conn.RemoteAddress
        }
    }

    try {
        $datos | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8
    }
    catch {
        Write-Host "⚠️ Error al escribir el archivo CSV. Puede estar en uso por otro proceso."
        return
    }

    $ips = $listaIP | Where-Object { $_ -and ($_ -ne '127.0.0.1') } | Sort-Object -Unique

    $logEntry = [PSCustomObject]@{
        timestamp = (Get-Date).ToString("s")
        task      = "Conexion-Internet"
        status    = "OK"
        output    = $csvPath
        ips_found = $ips.Count
    }
    $logEntry | ConvertTo-Json -Compress | Out-File -FilePath $jsonlLog -Append -Encoding utf8

    Write-Host "✅ Conexiones exportadas a: $csvPath"
    return $ips
}

function AbuseIPDB {
    $apiKey = "TU_API_KEY_AQUI"
    $url = "https://api.abuseipdb.com/api/v2/check"
    $lista_de_ips = Conexion_Internet

    $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
    $csvPath = "$env:USERPROFILE/Desktop/Reporte_IPs_$timestamp.csv"
    $jsonlReport = "$env:USERPROFILE/Desktop/Reporte_IPs_$timestamp.jsonl"
    $jsonlLog = "$env:USERPROFILE/Desktop/Logs.jsonl"

    $resultados = @()

    foreach ($ip in $lista_de_ips) {
        try {
            $Header = @{ 'Key' = $apiKey }
            $uri = "${url}?ipAddress=$ip&maxAgeInDays=90&verbose"
            $AbuseIPDB = Invoke-RestMethod -Method Get -Uri $uri -Headers $Header

            $Pais      = $AbuseIPDB.data.countryName
            $Tipo_Uso  = $AbuseIPDB.data.usageType
            $Reportes  = $AbuseIPDB.data.totalReports
            $WhiteListed = $AbuseIPDB.data.isWhitelisted
            $Confidence = $AbuseIPDB.data.abuseConfidenceScore

            $clasificacion = if ($WhiteListed -eq $true) { "Lista Blanca" } else { "Lista Negra" }

            $resultados += [PSCustomObject]@{
                IP              = $ip
                Pais            = $Pais
                TipoUso         = $Tipo_Uso
                Reportes        = $Reportes
                Clasificacion   = $clasificacion
                ConfidenceScore = $Confidence
            }

            $ipEntry = [PSCustomObject]@{
                timestamp       = (Get-Date).ToString("s")
                IP              = $ip
                Pais            = $Pais
                TipoUso         = $Tipo_Uso
                Reportes        = $Reportes
                Clasificacion   = $clasificacion
                ConfidenceScore = $Confidence
            }
            $ipEntry | ConvertTo-Json -Compress | Out-File -FilePath $jsonlReport -Append -Encoding utf8
        }
        catch {
            Write-Host "Error al consultar la IP $ip"
        }
    }

    $resultados | Export-Csv -Path $csvPath -NoTypeInformation -Encoding UTF8

    $logEntry = [PSCustomObject]@{
        timestamp = (Get-Date).ToString("s")
        task      = "AbuseIPDB"
        status    = "OK"
        output    = $csvPath
        ips_checked = $resultados.Count
    }
    $logEntry | ConvertTo-Json -Compress | Out-File -FilePath $jsonlLog -Append -Encoding utf8

    Write-Host "✅ Resultados exportados a: $csvPath y $jsonlReport"
}

switch ($accion) {
    "procesos" { Procesos-Activos }
    "conexion" { Conexion_Internet }
    "abuse"    { AbuseIPDB }
    default    { Write-Host "Acción no reconocida" }
}
