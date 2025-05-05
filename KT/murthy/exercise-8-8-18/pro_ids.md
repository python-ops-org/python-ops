
```
#!/bin/bash

INPUT_FILE="ids.csv"
OUTPUT_FILE="icto_summary.csv"

# Define platform mapping
vm_sources=("SPUDS" "SALT" "AUTH")
argo_sources=("Chanor")

# Write CSV header
echo "icto_ids,platform_type,source" > "$OUTPUT_FILE"

# Skip header and iterate over each ICTO ID
tail -n +2 "$INPUT_FILE" | while read -r icto_id; do
  # Call API
  response=$(curl -s "https://api.change.net/api/search/pdr?pageNumber=0&pageSize=100&sortBy=pdrId&direction=desc&query=icto%3A%22${icto_id}%22")

  # Extract all unique sources
  sources=$(echo "$response" | jq -r '.pdrs[]?.source' | sort -u | paste -sd "," -)

  # Initialize empty platform_type set
  platform_types=()

  # Check each source to map to platform type
  IFS=',' read -ra src_arr <<< "$sources"
  for src in "${src_arr[@]}"; do
    if [[ " ${vm_sources[@]} " =~ " ${src} " ]] && [[ ! " ${platform_types[@]} " =~ " VM " ]]; then
      platform_types+=("VM")
    elif [[ " ${argo_sources[@]} " =~ " ${src} " ]] && [[ ! " ${platform_types[@]} " =~ " ARGO " ]]; then
      platform_types+=("ARGO")
    fi
  done

  # Join platform_types array into comma-separated string
  platform_type=$(IFS=','; echo "${platform_types[*]}")

  

  # Write to CSV
  echo "$icto_id,$platform_type,$sources" >> "$OUTPUT_FILE"
done

echo "Report generated in $OUTPUT_FILE"


```
