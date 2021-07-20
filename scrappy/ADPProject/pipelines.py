# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class AdpprojectPipeline:
#    def process_item(self, item, spider):
#        return item

import logging
import sqlite3

class AdpprojectPipeline:
    def __init__(self):
        """
        Creating a local sqlite database and
        creating the schema if it doesn't exist already. 
        """
        self.connection = sqlite3.connect("./ozonedata.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS FandomData
            (
                is_available INTEGER
                price INTEGER
            )
        """
        )

    def process_item(self, item, spider):
        """
        Minimal item processing and inserting it into the
        database using the `self.connection` initialized
        in the constructor.
        """

        self.cursor.execute(
            """INSERT INTO FandomData (is_available, price) values (?, ?)""",
            (item["is_available", "price"])
        )

        self.connection.commit()
        logging.debug("Item stored {}".format(item["is_available", "price"]))
        return item
