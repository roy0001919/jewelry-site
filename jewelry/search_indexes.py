from haystack import indexes
# 修改此處，改成你自己的model
from .models import Goods

# 修改此處，類名為模型類的名稱+Index，比如模型類為Goods,則這裡類名為GoodsIndex
class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
    # 指明哪些欄位產生索引，產生索引的欄位，會作為前端檢索查詢的關鍵字；
    # document是指明text是使用的文件格式，產生欄位的內容在文件中進行描述；
    # use_template是指明在模板中被宣告需要產生索引；
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        """獲取模型類"""
        return Goods

    def index_queryset(self, using=None):
        """宣告滿足索引要求的返回的查詢集"""
        return self.get_model().objects.all()