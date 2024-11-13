# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClinicalDataItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    publicStudy = scrapy.Field()
    pmid = scrapy.Field()
    citation = scrapy.Field()
    groups = scrapy.Field()
    status = scrapy.Field()
    importDate = scrapy.Field()
    allSampleCount = scrapy.Field()
    sequencedSampleCount = scrapy.Field()
    cnaSampleCount = scrapy.Field()
    mrnaRnaSeqSampleCount = scrapy.Field()
    mrnaRnaSeqV2SampleCount = scrapy.Field()
    mrnaMicroarraySampleCount = scrapy.Field()
    miRnaSampleCount = scrapy.Field()
    methylationHm27SampleCount = scrapy.Field()
    rppaSampleCount = scrapy.Field()
    massSpectrometrySampleCount = scrapy.Field()
    completeSampleCount = scrapy.Field()
    readPermission = scrapy.Field()
    treatmentCount = scrapy.Field()
    structuralVariantCount = scrapy.Field()
    studyId = scrapy.Field()
    cancerTypeId = scrapy.Field()
    cancerType = scrapy.Field()
    referenceGenome = scrapy.Field()
