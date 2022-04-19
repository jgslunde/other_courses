data = read.delim("/home/jonas/github/other_courses/STK9900/oblig2/data/olympic.txt", header=TRUE, sep="")
fit.1 = glm(Total2000~offset(Log.athletes)+Total1996+Log.population+GDP.per.cap, data=data, family=poisson)
summary(fit.1)

fit.2 = glm(Total2000~offset(Log.athletes)+Log.population+GDP.per.cap, data=data, family=poisson)
summary(fit.2)

fit.3 = glm(Total2000~offset(Log.athletes)+Log.population, data=data, family=poisson)
summary(fit.3)
