data = read.delim("/home/jonas/github/other_courses/STK9900/oblig2/data/cirrhosis.txt", header=TRUE, sep="")
library(survival)

# Problem 3a)
surv.sex = survfit(Surv(data$time, data$status)~sex, data=data, conf.type="none")
surv.agegr = survfit(Surv(data$time, data$status)~agegr, data=data, conf.type="none")
surv.asc = survfit(Surv(data$time, data$status)~asc, data=data, conf.type="none")
surv.treat = survfit(Surv(data$time, data$status)~treat, data=data, conf.type="none")

png(file="/home/jonas/github/other_courses/STK9900/oblig2/report/figures/surv_sex.png")
plot(surv.sex, lty=1:2)
legend(1, 0.2, c("female", "male"), lty=1:2)
dev.off()

png(file="/home/jonas/github/other_courses/STK9900/oblig2/report/figures/surv_agegr.png")
plot(surv.agegr, lty=1:3)
legend(1, 0.2, c("<50", "50-65", ">65"), lty=1:3)
dev.off()

png(file="/home/jonas/github/other_courses/STK9900/oblig2/report/figures/surv_asc.png")
plot(surv.asc, lty=1:3)
legend(1, 0.2, c("none", "slight", "marked"), lty=1:3)
dev.off()

png(file="/home/jonas/github/other_courses/STK9900/oblig2/report/figures/surv_treat.png")
plot(surv.treat, lty=1:2)
legend(1, 0.2, c("prednisone", "placebo"), lty=1:2)
dev.off()

# Problem 3b)
survdiff(Surv(data$time, data$status)~sex, data=data)
survdiff(Surv(data$time, data$status)~agegr, data=data)
survdiff(Surv(data$time, data$status)~asc, data=data)
survdiff(Surv(data$time, data$status)~treat, data=data)

# Problem 3c)
fit.1 = coxph(Surv(data$time, data$status==1)~factor(sex)+age+factor(asc)+factor(treat), data=data)
summary(fit.1)
