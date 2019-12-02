# Moving (rolling) averages: SMA, WMA, EMA in R

install.packages("quantmod") # instalujemy biblioteke 
library(quantmod) # uruchamiamy ^ biblioteke

# przyklad 1 dla Idea Bank SA

start <- as.Date("2019-01-01") # data, od ktorej pobieramy dane; YYYY-MM-DD
end <- as.Date("2019-05-01") # data, do ktorej pobieramy dane; YYYY-MM-DD

getSymbols("IDA.WA", src = "yahoo", from = start, to = end) # pobieramy dane nt. Idea Bank SA z Yahoo Finance (symbol w Yahoo Finance: IDA.WA; https://is.gd/Q82Ck2); wartosci w PLN

head(IDA.WA) # sprawdzamy czy zaciagnelismy dobre dane

candleChart(IDA.WA, up.col = "green", dn.col = "red", theme = "white", name = "Idea Bank SA") # rysujemy wykres swiecowy
addSMA(n = 14, col = "blue") # rysujemy SMA z ostatnich 14 dni, kolor linii niebieski
addWMA(n = 14, col = "black") # rysujemy WMA z ostatnich 14 dni, kolor linii czarny
addEMA(n = 14, col = "orange") # rysujemy EMA z ostatnich 14 dni, kolor linii pomaranczowy

SMA(IDA.WA[,-c(1,2,3,5,6)], n = 14) # obliczenie SMA; wykluczamy wszystkie kolumny oprocz tej z danymi, ktore nas interesuja tj. 4: IDA.WA.Close

# przyklad 2 dla IBM  

start <- as.Date("2009-01-01")
end <- as.Date("2019-01-01")

getSymbols("IBM", src = "yahoo", from = start, to = end) # wartosci w USD

candleChart(IBM, up.col = "green", dn.col = "red", theme = "white")
addSMA(n = 90, col = "blue") # rysujemy SMA z ostatnich 90 dni
addWMA(n = 90, col = "black")
addEMA(n = 90, col = "orange")

EMA(IBM[,-c(1,2,3,5,6)], n = 90) # EMA z ostatnich 90 dni