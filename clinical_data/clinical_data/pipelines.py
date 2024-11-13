# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class ClinicalDataPipeline:
    def process_item(self, item, spider):
        return item


class SqlitePipeline:
    def __init__(self):
        self.conn = sqlite3.connect("clinical_data.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS clinical_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                publicStudy INTEGER,
                pmid TEXT,
                citation TEXT,
                groups TEXT,
                status INTEGER,
                importDate TEXT,
                allSampleCount INTEGER,
                sequencedSampleCount INTEGER,
                cnaSampleCount INTEGER,
                mrnaRnaSeqSampleCount INTEGER,
                mrnaRnaSeqV2SampleCount INTEGER,
                mrnaMicroarraySampleCount INTEGER,
                miRnaSampleCount INTEGER,
                methylationHm27SampleCount INTEGER,
                rppaSampleCount INTEGER,
                massSpectrometrySampleCount INTEGER,
                completeSampleCount INTEGER,
                readPermission INTEGER,
                treatmentCount INTEGER,
                structuralVariantCount INTEGER,
                studyId TEXT,
                cancerTypeId TEXT,
                cancerType TEXT,
                referenceGenome TEXT
            )
        """)
        self.conn.commit()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        self.cur.execute(
            """
            INSERT INTO clinical_data (
                name, description, publicStudy, pmid, citation, groups, status,
                importDate, allSampleCount, sequencedSampleCount, cnaSampleCount,
                mrnaRnaSeqSampleCount, mrnaRnaSeqV2SampleCount, mrnaMicroarraySampleCount,
                miRnaSampleCount, methylationHm27SampleCount, rppaSampleCount,
                massSpectrometrySampleCount, completeSampleCount, readPermission,
                treatmentCount, structuralVariantCount, studyId, cancerTypeId,
                cancerType, referenceGenome
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                item["name"],
                item["description"],
                item["publicStudy"],
                item["pmid"],
                item["citation"],
                item["groups"],
                item["status"],
                item["importDate"],
                item["allSampleCount"],
                item["sequencedSampleCount"],
                item["cnaSampleCount"],
                item["mrnaRnaSeqSampleCount"],
                item["mrnaRnaSeqV2SampleCount"],
                item["mrnaMicroarraySampleCount"],
                item["miRnaSampleCount"],
                item["methylationHm27SampleCount"],
                item["rppaSampleCount"],
                item["massSpectrometrySampleCount"],
                item["completeSampleCount"],
                item["readPermission"],
                item["treatmentCount"],
                item["structuralVariantCount"],
                item["studyId"],
                item["cancerTypeId"],
                item["cancerType"],
                item["referenceGenome"],
            ),
        )
        self.conn.commit()
        return item
