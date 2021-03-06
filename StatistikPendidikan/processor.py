import requests
import lxml.html as lh
import json
from StatistikPendidikan.get import getHtmlResponse

def getGambaranUmumSekolah(tingkatan,tahun_ajaran):
	doc = getHtmlResponse(tingkatan,tahun_ajaran,"1")
	table_description = doc.xpath('//table/thead/tr')
	table_description = table_description[0:len(table_description)-2]
	extracted_table_data = {}
	extracted_table_data['id_tabel'] = table_description[0].xpath('th')[0].text_content().replace('TABEL / TABLE : ','')
	extracted_table_data['tahun'] = table_description[3].text_content().replace('TAHUN / YEAR : ','')
	extracted_table_data['nama_tabel'] = table_description[1].text_content()
	raw_data = doc.xpath('//table/tbody/tr')
	for data in raw_data:
	  cols = data.xpath('td')
	  if len(cols[0].text_content()) >1:
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()] = {}
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['negeri'] = cols[2].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['swasta'] = cols[4].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['jumlah'] = cols[6].text_content().replace(',','')
	return extracted_table_data

def getGambaranUmumSekolahPerProvinsi(tingkatan,tahun_ajaran):
	doc = getHtmlResponse(tingkatan,tahun_ajaran,"2")
	table_description = doc.xpath('//table/thead/tr')
	table_description = table_description[0:len(table_description)-2]
	extracted_table_data = {}
	extracted_table_data['id_tabel'] = table_description[0].xpath('th')[0].text_content().replace('TABEL / TABLE : ','')
	extracted_table_data['tahun'] = table_description[4].text_content().split(':')[1].strip()
	extracted_table_data['nama_tabel'] = table_description[1].text_content().strip()
	raw_data = doc.xpath('//table/tbody/tr')
	for data in raw_data:
	  cols = data.xpath('td')
	  if len(cols[0].text_content()) >1:
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()] = {}
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Sekolah'] = cols[2].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Siswa'] = cols[3].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Mengulang'] = cols[4].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Putus Sekolah'] = cols[5].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['KS & Guru'] = cols[6].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Tenaga Kependidikan'] = cols[7].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Rombel'] = cols[8].text_content().replace(',','')
	    extracted_table_data[cols[1].text_content().split("/")[0].strip()]['Ruang Kelas'] = cols[9].text_content().replace(',','')
	return extracted_table_data
