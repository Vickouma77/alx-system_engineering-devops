# Regular expression
A regular expression (regex or regexp) is a sequence of characters that defines a search pattern. Regex can be used to check if a string contains the specified search pattern. It is commonly used in text processing, string manipulation, and validation.

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:
```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```

Oniguruma is a regular expression library that is written in C programming language. It supports a wide range of regular expression syntax, including some advanced features like lookahead/behind assertions and named capture groups. It is used in many programming languages, text editors, and other tools for processing text. The syntax and usage of regular expressions in Oniguruma may vary slightly compared to other regex libraries
example of implementation
```
require 'oniguruma'

# Create a regular expression pattern
pattern = Oniguruma::ORegexp.new("^[a-z]+$")

# Check if the pattern matches a string
if pattern =~ "hello"
  puts "Match found!"
else
  puts "No match found."
end
```

## About
```Regex```
```DevOps```
