# data-scrapy
Web scrapping for Clinical Data

```sh
python3 -m venv venv
source venv/bin/activate
pip install scrapy
```

launch.json

```json
{
    "version": "0.1.0",
    "configurations": [
        {
            "name": "Python: Launch Scrapy Spider",
            "type": "debugpy",
            "request": "launch",
            "module": "scrapy",
            "python": "${workspaceFolder}/venv/bin/python",
            "args": [
                "crawl",
                "clinical_data_spider"
            ],
            "cwd": "${workspaceFolder}/clinical_data",
            "console": "integratedTerminal"
        }
    ]
}
```

If we want to save the data to a JSON file we can use the -O option, followed by the name of the file.

```sh
cd clinical_data 
scrapy crawl clinical_data_spider -O datasets.json
```

run debug to save to db
