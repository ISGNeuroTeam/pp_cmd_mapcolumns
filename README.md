# pp_cmd_mapcolumns
Postprocessing command "mapcolumns"
## Description
Command renames columns in dataframe using subsearch with column names mapping

### Arguments
- mapping_df - subsearch argument, required. Subseach must return dataframe with column mapping
- source - keyword argument, not required, default is `metric_name`. Column name in subsearch, column with old names.
- target - keyword argument, not required, default is `metric_long_name`. Column name in subsearch, column with new names.


### Usage example
```
... | mapcolumns source=sourceColumn target=targetedColumn [ otl_v1 <# | inputlookup mymaplookup.csv #>]
```
```
query: readFile map.csv
  old_names    new_names
0         A   A_new_name
1         B   B_new_name
```
```
query: readFile d.csv
         date         A         B         C         D
0  2013-01-01  1.075770 -0.109050  1.643563 -1.469388
1  2013-01-02  0.357021 -0.674600 -1.776904 -0.968914
2  2013-01-03 -1.294524  0.413738  0.276662 -0.472035
3  2013-01-04 -0.013960 -0.362543 -0.006154 -0.923061
4  2013-01-05  0.895717  0.805244 -1.206412  2.565646
```
```
query:  readFile d.csv | mapcolumns source=old_names, target=new_names [readFile map.csv]
         date   A_new_name   B_new_name         C         D
0  2013-01-01     1.075770    -0.109050  1.643563 -1.469388
1  2013-01-02     0.357021    -0.674600 -1.776904 -0.968914
2  2013-01-03    -1.294524     0.413738  0.276662 -0.472035
3  2013-01-04    -0.013960    -0.362543 -0.006154 -0.923061
4  2013-01-05     0.895717     0.805244 -1.206412  2.565646
```


## Getting started
### Installing
1. Create virtual environment with post-processing sdk 
```bash
    make dev
```
That command  
- downloads [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates link to current command in postprocessing `pp_cmd` directory 

2. Configure `otl_v1` command. Example:  
```bash
    vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/otl_v1/config.ini
```
Config example:  
```ini
[spark]
base_address = http://localhost
username = admin
password = 12345678

[caching]
# 24 hours in seconds
login_cache_ttl = 86400
# Command syntax defaults
default_request_cache_ttl = 100
default_job_timeout = 100
```

3. Configure storages for `readFile` and `writeFile` commands:  
```bash
   vi ./venv/lib/python3.9/site-packages/postprocessing_sdk/pp_cmd/readFile/config.ini
   
```
Config example:  
```ini
[storages]
lookups = /opt/otp/lookups
pp_shared = /opt/otp/shared_storage/persistent
```

### Run mapcolumns
Use `pp` to run mapcolumns command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  mapcolumns 
```
## Deploy
Unpack archive `pp_cmd_mapcolumns` to postprocessing commands directory