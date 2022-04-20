data = read.delim("/home/jonas/github/other_courses/STK9900/oblig2/data/crabs.txt", header=TRUE, sep="")

# Problem 1a
fit.width = glm(y~width, data=data, family=binomial)
summary(fit.width)

fit.weight = glm(y~weight, data=data, family=binomial)
summary(fit.weight)

# Problem 1c
fit.color = glm(y~factor(color), data=data, family=binomial)
summary(fit.color)

fit.spine = glm(y~factor(spine), data=data, family=binomial)
summary(fit.spine)

# Problem 1d
fit.all = glm(y~width+weight+factor(color)+factor(spine), data=data, family=binomial)
summary(fit.all)

fit.width.color = glm(y~width+factor(color), data=data, family=binomial)
summary(fit.width.color)

fit.width.spine = glm(y~width+factor(spine), data=data, family=binomial)
summary(fit.width.spine)

plot(data$weight, data$width)

# Problem 1e
fit.1 = glm(y~width+width*weight, data=data, family=binomial)
summary(fit.1)

fit.2 = glm(y~width+width*factor(color), data=data, family=binomial)
summary(fit.2)

fit.3 = glm(y~width+width*factor(spine), data=data, family=binomial)
summary(fit.3)

fit.4 = glm(y~width+weight*factor(color), data=data, family=binomial)
summary(fit.4)

fit.5 = glm(y~width+weight*factor(spine), data=data, family=binomial)
summary(fit.5)

fit.6 = glm(y~width+factor(color)*factor(spine), data=data, family=binomial)
summary(fit.6)
