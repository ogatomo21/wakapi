# WakAPI

## What is this?

"Waka"Time + "API" = WakAPI

WakAPIはWakaTimeのAPIをPythonで簡単に使えるライブラリです。

## 使用例

### total

`wakapi.total(secret, sec)` 
- Secret* WakaTime API Secret
- sec デフォルトはfalse。falseだとjsonをそのまま、trueだと時間のみをJSONで返します。

#### 例

`wakapi.total("waka_*****", False)`

### date

`wakapi.date(secret, date, sec)` 
- Secret* WakaTime API Secret
- date* 取得したい日付をYYYY-MM-DDで指定します。
- sec デフォルトはfalse。falseだとjsonをそのまま、trueだと時間のみをJSONで返します。

#### 例

`wakapi.total("waka_*****", "2011-10-10", False)`