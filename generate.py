import json

# YOKDUMB HTML Generator
# This script generates HTML files for various score types (MF, TM, SOZ, DIL)
# by loading data from corresponding JSON files and formatting it into an HTML table.

score_types = ["MF", "TM", "SOZ", "DIL"]

for score_type in score_types:
  page_template = f"""
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{score_type} Verileri</title>
<link rel="stylesheet" href="/yokdumb/static/style.css" />
</head><body><div id="main">
<h1>{score_type} Verileri</h1>
<table><tr><th>ID</th><th>Üniversite</th><th>Fakülte</th><th>Bölüm</th><th>Öğrenim Türü</th><th>Kontenjan</th><th>Yerleşen</th><th>Sıralama</th></tr>
{{}}</table></div></body>
</html>"""

  with open(f"./data/{score_type}.json", encoding="utf-8") as json_file:
    programs = json.load(json_file)
    programs_html = ""

    for program in programs:
      program_html = f"""<tr>
  <td><a href="https://yokatlas.yok.gov.tr/lisans.php?y={program["id"]}" target="_blank">{program["id"]}</a></td>
  <td>{program["university"]}</td>
  <td>{program["faculty"]}</td>
  <td>{program["degree"]}</td>
  <td>{program["educationType"]}</td>
  <td><span><strong>2023</strong>: {program["capacity"]["2023"]}</span>
  <span><strong>2022</strong>: {program["capacity"]["2022"]}</span>
  <span><strong>2021</strong>: {program["capacity"]["2021"]}</span>
  <span><strong>2020</strong>: {program["capacity"]["2020"]}</span></td>
  <td><span><strong>2023</strong>: {program["placement"]["2023"]}</span>
  <span><strong>2022</strong>: {program["placement"]["2022"]}</span>
  <span><strong>2021</strong>: {program["placement"]["2021"]}</span>
  <span><strong>2020</strong>: {program["placement"]["2020"]}</span></td>
  <td><span><strong>2023</strong>: {program["ranking"]["2023"]}</span>
  <span><strong>2022</strong>: {program["ranking"]["2022"]}</span>
  <span><strong>2021</strong>: {program["ranking"]["2021"]}</span>
  <span><strong>2020</strong>: {program["ranking"]["2020"]}</span></td>
  </tr>"""
      programs_html += program_html

    page_html = page_template.format(programs_html)
    with open(f"./result/{score_type}.html", "w+", encoding="utf-8") as html_file:
      html_file.write(page_html)
    