

| Variable | Description |
|----------|-------------|
| `$#`     | Stores the number of command-line arguments passed to the shell script. |
| `$?`     | Stores the exit status of the last executed command. |
| `$0`     | Stores the name of the script or shell program. |
| `$1`, `$2`, ... | Stores the first, second, etc., command-line arguments individually. |
| `$*`     | Stores all command-line arguments as a single word (space-separated). Not recommended in most cases. |
| `"$@"`   | Stores all command-line arguments, each quoted separately (`"$1"`, `"$2"`, ...). Recommended for looping over arguments. |
| `$!`     | Stores the process ID of the most recently executed background process. |
| `$$`     | Stores the process ID of the current shell. |
| `#!`     | Shebang: specifies the interpreter that should execute the script. |
| `$-`     | Displays the current shell flags (e.g., `-x`, `-v`, etc.). |
