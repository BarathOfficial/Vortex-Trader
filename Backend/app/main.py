
from app.collectors.marketaux import MarketauxCollector

collector = MarketauxCollector()

print("ENTITY TYPES")
print(collector.fetch_entity_types())

print("INDUSTRIES")
print(collector.fetch_entity_industries())

print("ENTITY SEARCH")
print(collector.fetch_entity_search("Reliance Industries"))

print("NEWS SOURCES")
print(collector.fetch_news_sources())

print("FINANCIAL NEWS")
print(collector.fetch_news())

