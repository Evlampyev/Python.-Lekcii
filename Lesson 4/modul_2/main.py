import html_creater
import xml_generator
import data_provider as dp

# print(html_creater.create())
# print(xml_generator.create())


html_creater.new_create(xml_generator.new_create(dp.data_collection()))
