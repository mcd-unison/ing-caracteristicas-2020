# Priero vamos a bajar dos bases de juguete de Kaggle:
#    https://www.kaggle.com/mirichoi0218/insurance/
#    https://www.kaggle.com/c/titanic
#
# Como te piden que estés registrado y aceptes términos de kaggle,
# pues la tendremos que bajar a pie.


#--------- Primer opción (sencilla pero carismática) ----------------

# Aqui va tu propio directorio o lo puedes hacer a pie
setwd("~/Documents/cursos/IC-MCD-Unison/codigos/EDA")

library(summarytools) 
library(readr) 
df <- read_csv("insurance.csv") 

a <- dfSummary(df)


view(dfSummary(df), file="insurance-summarytools.html")

#---------- Segunda opción (mas acá) ---------------------------------

library(explore) 
df <- read_csv("insurance.csv") 
explore(df)

#--------- Tercera opción (la más perrona) ---------------------------

library('dataMaid')  
df <- read_csv("insurance.csv")
makeDataReport(df,                
               render = FALSE,
               file = "insurance_dataMaid.Rmd",
               replace = TRUE)

