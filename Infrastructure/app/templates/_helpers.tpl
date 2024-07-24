{{/*
This file contains functions that are used across other templates to avoid repetition.
*/}}
{{/* Defines a template named finals-chart.fullname. */}}
{{- define "finals-chart.fullname" -}}
{{/*Checks if fullnameOverride is set in the values.yaml */}}
{{- if .Values.fullnameOverride -}}
{{/*Overrides the name with 63 characters, without trailing htphens*/}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{/* if fullnameoverride isn't set, use default */}}
{{- $name := default .Chart.Name .Values.nameOverride -}}
{{/* Combines the release name and chart name, */}}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{/* Ends the else-if and the template def */}}
{{- end -}}
{{- end -}}

{{/*
Common labels
*/}}
{{/* Defines a template named finals-chart.labels */}}
{{- define "finals-chart.labels" -}}
{{/* Adds a label with the chart name and version. */}}
helm.sh/chart: {{ include "finals-chart.chart" . }}
{{/* Includes selector labels. */}}
{{ include "finals-chart.selectorLabels" . }}
{{/* Checks if AppVersion is set, add v label. */}}
{{- if .Chart.AppVersion }}
app.kubernetes.io/version: {{ .Chart.AppVersion | quote }}
{{- end }}
{{/*Adds a managed-by label*/}}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Chart version
*/}}
{{/*Defines a template named finals-chart.chart, Combines the chart name and version*/}}
{{- define "finals-chart.chart" -}}
{{ .Chart.Name }}-{{ .Chart.Version }}
{{- end -}}

{{/*
Selector labels
*/}}
{{/*Defines a template named finals-chart.selectorLabels*/}}
{{- define "finals-chart.selectorLabels" -}}
{{/*Adds a name label*/}}
app.kubernetes.io/name: {{ include "finals-chart.name" . }}
{{/*Adds an istance label*/}}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Simple name
*/}}
{{/*Defines a template named finals-chart.name*/}}
{{- define "finals-chart.name" -}}
{{- if .Values.nameOverride -}}
{{- .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}