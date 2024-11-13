
from clinical_data.items import ClinicalDataItem
import scrapy

import json


class ClinicalDataSpider(scrapy.Spider):
    # name - a class attribute that gives a name to the spider. We will use this when running our spider later scrapy crawl <spider_name>
    # allowed_domains - a class attribute that tells Scrapy that it should only ever scrape pages of the books.toscrape.com domain. This prevents the spider going rouge and scraping lots of websites. This is optional.
    # start_urls - a class attribute that tells Scrapy the first url it should scrape.
    # parse - the parse function is called after a response has been recieved from the target website.

    name = "clinical_data_spider"

    def start_requests(self):
        # url = "https://www.cbioportal.org/datasets"
        # since the page is written in react, we can get the json instead of parsing through html
        url = "https://www.cbioportal.org/api/studies?projection=DETAILED"

        # next step
        # get a list of url by extracting studyId from the list
        # go to each url and run the following url

        # next step is select one item by studyId
        # then inspect network tab to see fetch calling which apis

        # https://www.cbioportal.org/study/summary?id=paac_jhu_2014
        # https://www.cbioportal.org/study/summary?id=nbl_msk_2023

        # https://www.cbioportal.org/api/studies?projection=SUMMARY GET
        # https://www.cbioportal.org/api/clinical-attributes/fetch
        # https://www.cbioportal.org/api/molecular-profiles/fetch
        # https://www.cbioportal.org/api/filtered-samples/fetch
        # https://www.cbioportal.org/api/custom-driver-annotation-report/fetch
        # https://www.cbioportal.org/api/treatments/display-patient
        # https://www.cbioportal.org/api/treatments/display-sample
        # https://www.cbioportal.org/api/clinical-event-type-counts/fetch
        # https://www.cbioportal.org/api/genes?projection=SUMMARY GET
        # https://cbioportal-datahub.s3.amazonaws.com/study_list.json GET
        # https://www.cbioportal.org/api/molecular-profile-sample-counts/fetch
        #
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        datasets = response.json()
        for data in datasets:
            clinical_data_item = ClinicalDataItem(
                name=data.get("name", ""),
                description=data.get("description", ""),
                publicStudy=data.get("publicStudy", False),
                pmid=data.get("pmid", ""),
                citation=data.get("citation", ""),
                groups=data.get("groups", []),
                status=data.get("status", ""),
                importDate=data.get("importDate", ""),
                allSampleCount=data.get("allSampleCount", 0),
                sequencedSampleCount=data.get("sequencedSampleCount", 0),
                cnaSampleCount=data.get("cnaSampleCount", 0),
                mrnaRnaSeqSampleCount=data.get("mrnaRnaSeqSampleCount", 0),
                mrnaRnaSeqV2SampleCount=data.get("mrnaRnaSeqV2SampleCount", 0),
                mrnaMicroarraySampleCount=data.get("mrnaMicroarraySampleCount", 0),
                miRnaSampleCount=data.get("miRnaSampleCount", 0),
                methylationHm27SampleCount=data.get("methylationHm27SampleCount", 0),
                rppaSampleCount=data.get("rppaSampleCount", 0),
                massSpectrometrySampleCount=data.get("massSpectrometrySampleCount", 0),
                completeSampleCount=data.get("completeSampleCount", 0),
                readPermission=data.get("readPermission", ""),
                treatmentCount=data.get("treatmentCount", 0),
                structuralVariantCount=data.get("structuralVariantCount", 0),
                studyId=data.get("studyId", ""),
                cancerTypeId=data.get("cancerTypeId", ""),
                cancerType=json.dumps(data.get("cancerType", "")),
                referenceGenome=data.get("referenceGenome", ""),
            )

            yield clinical_data_item

        # for dataset in datasets:
        # this return the datasets
        # yield dataset

        # build the url for each item and fetch it here
        # dataset_url = (
        #     "https://www.cbioportal.org/study/clinicalData?id=" + dataset["studyId"]
        # )

        # yield scrapy.Request(dataset_url, callback=self.parse_dataset_page)

    # def parse_dataset_page(self, response):
    #     item = response
    #     yield {}