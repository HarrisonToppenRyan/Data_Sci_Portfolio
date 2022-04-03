import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index() 

clicks_pivot = clicks_by_source.pivot(
  index = 'utm_source',
  columns = 'is_click',
  values = 'user_id'
)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

ad_clicks.groupby('experimental_group')\
    .user_id.count()\
    .reset_index()

new_pivot = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

clicks_pivot2 = new_pivot.pivot(
  index = 'experimental_group',
  columns = 'is_click',
  values = 'user_id'
)



a_clicks = ad_clicks[ad_clicks.experimental_group
   == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group
   == 'B']

a_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()

b_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  index = 'day',
  columns = 'is_click',
  values = 'user_id'
).reset_index()

a_pivot['percent_clicked'] = a_pivot[True] / (a_pivot[True] + a_pivot[False])

b_pivot['percent_clicked'] = b_pivot[True] / (b_pivot[True] + b_pivot[False])
print(a_pivot)
print(b_pivot)





