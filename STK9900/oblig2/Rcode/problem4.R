install.packages("lme4")
library(lme4)
data(sleepstudy)
sleepstudy

# Problem 4a)
png(file="/home/jonas/github/other_courses/STK9900/oblig2/report/figures/sleepstudy.png")
plot(sleepstudy$Days, sleepstudy$Reaction)
dev.off()

mean(sleepstudy$Reaction[sleepstudy$Days==0])
mean(sleepstudy$Reaction[sleepstudy$Days==9])

sleepstudy2 = sleepstudy[sleepstudy$Days==0 | sleepstudy$Days==9]
fit.aov = aov(Days~Reaction, data=sleepstudy)
summary(fit.aov)

# Problem 4b)
fit.lm = lm(Reaction~Days, data=sleepstudy)
summary(fit.lm)

fit.lm2 = lm(Reaction~Days+factor(Subject), data=sleepstudy)
summary(fit.lm2)

# Problem 4c)
library(nlme)
fit.random = lme(Reaction~factor(Days), random=~1|Subject, data=sleepstudy)
summary(fit.random)
37.08727^2/(37.08727^2 + 31.42592^2)
