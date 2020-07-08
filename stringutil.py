import re
from japanera import Japanera, EraDate, Era
class StringUtil():
  @staticmethod
  def extract_date_from_header(header: str):
    return header
  
  @staticmethod
  def extract_date_from_title(title: str):
    """extract date object from title string

    Args:
        title (str): Title string, like マイナンバーカード交付状況（令和2年6月1日現在)

    Returns:
        datetime: Date object
    """
    janera = Japanera()
    match =  re.search(r'[（(](.*)[)）]', title)
    if (not match):
      return False
    datesource = re.search(r'([^0-9元]*)([0-9元]*)年(.*)月(.*)日', match.groups()[0])
    mydate = janera.strptime('{0}{1}年{2}月{3}日'.format(
      datesource.groups()[0],
      datesource.groups()[1].replace('元','1').zfill(2),
      datesource.groups()[2].zfill(2),
      datesource.groups()[3].zfill(2)
    ), "%-E%-o年%m月%d日")
    return mydate[0]

  @staticmethod
  def to_number(text: str):
    """return number object if the text is number, otherwise return text

    Args:
        text (str): text
    """
    if (text.replace(',', '').replace('.', '').replace('-', '').replace('%', '').isnumeric()):
      if ('.' in text):
        return float(text.replace(',', '').replace('%',''))
      else:
        return int(text.replace(',', '').replace('%',''))
    return text
