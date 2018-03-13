data <- read.table("http://www.uio.no/studier/emner/matnat/math/STK1100/v18/dodelighet-felles.txt",
                   header = TRUE)

data <- data[data$ald>=35,]

data$p_x <- data$ald - 35

pdf("2c.pdf")
plot(data$p_x, data$dod, xlab="x", ylab="p(x)")
dev.off()