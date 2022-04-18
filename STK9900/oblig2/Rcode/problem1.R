data = read.delim("/home/jonas/github/other_courses/STK9900/oblig2/data/crabs.txt", header=TRUE, sep="")

# Problem 1a
fit.width = glm(y~width, data=data, family=binomial)
summary(fit.width)

fit.weight = glm(y~weight, data=data, family=binomial)
summary(fit.weight)

fit.color = glm(y~factor(color), data=data, family=binomial)
summary(fit.color)

fit.spine = glm(y~factor(spine), data=data, family=binomial)
summary(fit.spine)

fit.all = glm(y~width+weight+factor(color)+factor(spine), data=data, family=binomial)
summary(fit.all)

fit.width.color = glm(y~width+factor(color), data=data, family=binomial)
summary(fit.width.color)

fit.width.spine = glm(y~width+factor(spine), data=data, family=binomial)
summary(fit.width.spine)

plot(data$weight, data$width)

