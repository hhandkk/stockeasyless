import get_10jqka_hotquote_rank
import get_quote_txn
import get_10jqka_skyrocket
import get_10jqka_industry
import get_10jqka_concept
from get_index_shanghai_exchange_time_sharing import get_index_shanghai_exchange_time_sharing_det

#获取当前股市最新数据，一天两次
get_quote_txn.get_current_block_txn()

#获取同花顺热板个股排行数据，一天两次
get_10jqka_hotquote_rank.get_10jqka_hotblock()

#获取同花顺个股飙升版个股数据，一天两次
get_10jqka_skyrocket.get_10jqka_skyrocket()

#同花顺概念热板
get_10jqka_concept.get_10jqka_concept()

#同花顺业务热榜

get_10jqka_industry.get_10jqka_industry()

#t日大盘分时数据
get_index_shanghai_exchange_time_sharing_det()

#t日