#####################################################################################
# matheus carrijo
######################################################################################
println("matheus")

x = rand(10)

x
m = [1 2; 4 0.2]

m*m'


cos(pi/360)

@doc cos

# example of a function

function matheus(x)
    x^2
end

matheus(25)

for i in 1:4
    i += i
    print(i)
end # for

@show f(2)

x = 10
"minha nota foi = $x"

# for concatanate string we use *

"Matheus" * "gabi"

"matheus gabriela"

nome = "matheus carrijo de brito"

print(nome)

strip("matheus")

strip("foobar")

replace(nome, "carrijo" => "Carrijo")

s = "Matheus don't surf"

split(s)

replace(nome, "carrijo" => "Carrijo")

##########################################################################

# subsetting a string
nome[2:10]

# dictionary

d = Dict("name" => "Frodo", "age" => 33, "type" => 55)

d["type"]

actions = ["futebol", "tênis"]

for i in 1:2
    println("matheus vai jogar $(actions[i])")
end

x_values = 1:5

for i in x_values
    println(i*i)
end

@time for i in x_values
        println(i*3)
       end

using Distributions

x = rand(1000)

mean(x)

using Plots

plot(x)

histogram(x)


for i in 1:1000
    x[i] = (x[i] - mean(x))/std(x)
end

histogram(x)
plot(x)

countries = ("Germany", "EUA", "England")
cities = ("Berlin", "Washington", "London")

for (country, city) in zip(countries, cities)
    println("the capital of $country is $city")
end
