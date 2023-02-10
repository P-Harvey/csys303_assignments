library(ggplot2)

n = 10^6

a = rnorm(n, 0, 2/3)^3
b = rnorm(n, 0, 2/3)^3
c = (a - b)^3
data = data.frame(cbind(a,b,c))

fig <- ggplot(data) + geom_point(aes(x=a,y=b),
                                 color = 'darkgreen',
                                 alpha = abs(c)/(n/100),
                                 size = abs(c)/n) + theme_minimal()
fig