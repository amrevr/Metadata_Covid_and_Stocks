# Stock Data Metadata: yfinance
The data was sourced from "Yahoo Finance" by using their API in an advertent way by using a popular opensource Python Package.

## Ticker Symbol
Ticker symbols are unique combinations of letters that identify publicly traded companies and their stocks, facilitating easy reference and communication in financial markets. They enable investors to quickly distinguish between different stocks and standardize trading across various exchanges. The date range for analyzing historical market data is crucial as it provides context for stock performance, allowing for comparative analysis, identification of seasonal trends, and understanding the impact of broader economic events.

## Frequency
The data is analyzed from December 1, 2021, to March 31, 2022 as it encompasses peak COVID-19 conditions, influencing market dynamics in the US.

The frequency of the data—daily, weekly, or monthly—affects trend analysis. Daily data captures short-term fluctuations and volatility, which is useful for tactical trading decisions. In contrast, weekly or monthly data smooths out these fluctuations, providing clearer insights into long-term trends and overall market health.

This comprehensive understanding of ticker symbols, date ranges, and data frequency allows investors to make informed decisions based on the historical performance and context of the stocks they are interested in. The provided code effectively retrieves and saves relevant historical data for further analysis.

## Data Fields
I used common fields like Open, High, Low, Close, Volume, and Adjusted Close for each stock csv because it is the standardized framework that is used by most people who are interested in this data. 

Each field offers unique insights: 
- The Open establishes the starting point of trading. 
- High and Low indicate price peaks and troughs, helping to identify resistance and support levels. 
- Close is crucial for technical analysis, serving as a key reference point. 
- Volume reflects trading activity and investor sentiment. 
- Adjusted Close accounts for dividends and splits, providing a clearer picture of a stock's true value over time. 

Together, these fields can be used to perform any sort of meaningful analysis, enabling investors to make informed decisions based on historical trends and market behavior.

## Currency

The prices are denominated in U.S. dollars (USD), providing a consistent framework for domestic investors as my goal was to analyze the impact of COVID-19 on the US Stock Market exclusively. Currency fluctuations are also harder to analyze when looking at multiple currencies as there might other localized factors involved that cause certain currencies to flourish/dip. 

Regarding US Stocks, the any currency fluctuations occurred primarily through the appreciation of the U.S. dollar as investors sought safety. A stronger dollar made U.S. exports more expensive, adversely affecting companies reliant on international sales and potentially dampening stock prices. For foreign investors, currency volatility meant that returns on U.S. investments could vary based on exchange rates, influencing their willingness to invest. Additionally, the dollar's fluctuations mirrored market sentiment about economic recovery, as it reacted to stimulus measures and vaccine rollouts. Overall, these dynamics highlight how currency movements shaped the stock market landscape during the pandemic, affecting investor behavior and corporate strategies.

## Adjustments

Any adjustments are crucial for accurately reflecting historical prices and ensuring reliable comparisons across different periods. For instance, stock splits can distort perceptions of stock performance if not accounted for, while dividend payments provide insights into a company's financial health. Accurate adjustments enable investors to evaluate Total Return, which incorporates both price appreciation and dividends, guiding informed investment decisions. 

These adjustments have not been performed yet, but would definitely be incorporated when any analysis is conducted.

## Limitations
Since the data is technically from a third party source, the information can possibly be incorrect. But considering how big of a name Yahoo is, it can probably be assumed to be reliable. The data is also limited to the spikes of COVID by cases. This does not incorporate the impact of mass hysteria or any of the bandwagoning that occured with COVID during its inital few months of significant but not alarming levels of case rise(s). Considering these factors, any analysis performed would be only useful for analyzing the impact of COVID at its peak not during its overall duration. 

# COVID-19 Data Metadata
Data is sourced from OWID, which gets its data from governmental health organizations, and other health data aggregators.

## Date Range
The selection of COVID-19 data from December 1, 2021 to March 31, 2022, is critical for understanding the pandemic's dynamics during a peak period marked by the rapid spread of the Omicron variant. This timeframe captures significant fluctuations in case numbers and hospitalizations, alongside ongoing vaccination efforts, including booster shots. Analyzing this timeframe provides the best possible baseline for analyzing the overall impact of COVID 19 on the US Stock Market, as this would be one of the major points of time where the market was impacted to a larger extent than other periods solely based on the number cases being discovered every day.

## Geographical Coverage
The focus of the data is in the United States mainly so it encompasses all cases reported in any US territories. Thankfully, the label of 'United States of America' only considers mainland US cases so any cases on American military bases etc. are not included in this tally.

## Data Fields
The data fields include common virus related metrics like new cases, total cases, new deaths, total deaths, population, and testing rates, are essential for understanding the pandemic's impact. 
- New cases track the number of infections over specific periods. 
- Total cases reflect cumulative infections. 
- New and total deaths provide insights into the pandemic's severity and mortality impact. 
- Population data contextualizes these metrics, allowing for per capita calculations that clarify the virus's effects relative to the population size. 
- Testing rates indicate the number of tests conducted per population unit, which is crucial for identifying cases and controlling outbreaks.

Together, these metrics (and others which encompass these sentiments in more detail) offer vital insights that inform public health responses and resource allocation, enhancing overall pandemic management.

## Frequency
Distinguishing between daily and cumulative counts in COVID-19 metadata is essential for understanding the pandemic's progression. 

Daily counts provide real-time insights into new cases, deaths, and tests conducted, allowing public health officials to identify trends and assess the effectiveness of short-term interventions. 

In contrast, cumulative counts represent the total number of cases and deaths since the pandemic began, offering a broader context that informs long-term evaluations and resource allocation. Together, these metrics enable a nuanced understanding of both immediate fluctuations and overall trends, supporting informed decision-making and effective public health strategies in response to the evolving crisis.

## Limitations
The data is not split by state so I cannot analyze of rapid spread of COVID in major sectors for a specific stock i.e Wall Street for anything Finance related or the Bay Area for anything Tech related dropping in pricing W.R.T case rises in the area. However, since the economy is so interconnected, an overall increase in COVID-19 cases most definitely impacted all sectors being analyzed in some way (either positive or negatively).

Key factors like policy changes, vaccination rates, and the emergence of variants influence case surges and declines, and without this context, analysts may lead to misinterpretation in data. Additionally, seasonal behaviors, such as holiday gatherings, can skew transmission rates, while healthcare responses and public sentiment further shape outcomes. Since this data should not be used at face-value, but rather as a tool to aid any overall meaningful analysis, the impact of this external factor can be mitigated somewhat.
