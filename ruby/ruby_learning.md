# RUBY
- Link: https://www.theodinproject.com
## 1. Introduction
- Strongly object oriented language
- Everything is object, event basic data types

## 2. Variable
- numbers (integer + float)
- string
- symbol
- boolean (**true**, **false**, and **nil**)
### 2.1. Numbers
#### 2.1.1. Interger
#### 2.1.2. Float
### 2.2. String
### 2.3. Symbol
- look like string
- the same symbol has the same id
### 2.4. Boolean

## 3. Input & Output 
### 3.1. Input
- use $gets$ to read input (always end with new line, use chomp to trim the input)
### 3.2. Output
- could use $print$ or $puts$
- $print$ does not append new line at the end but $puts$ does

## 4. Loop
## 4.1. Loop
- use $loop$ $do$ $end$ for infinite loop, break until call $break$
## 4.2. While loop
- use $while$ \{condition\} $do$ $end$
## 4.3. Until loop
- use $until$ \{condition\} $do$ $end$
## 4.4. Range
- inclusive loop: $from$ **..** $to$ <-> [from, to)
- exlusive loop: $from$ **...** $to$ <-> [from, to]
## 4.5. #times loop
- $integer$.times $do$ 

## 5. Array
- similar data types in one array
### 5.1. Creating Array
- $\#new(size, default_value)$ method 
### 5.2. Adding and remove
- $\#pop$ and $\#shift$
- $\#unshift$ and $\#push$
### 5.3. Adding and substracting
- $+$ OR $\#concat$ operator for adding 2 arrays
- $-$ operator for subtracting 2 arrays

## 6. Methods
### 6.1. Return
- explicit return or use $return$
### 6.2. Bang method
- method does not override or re-assign the value of object -> need to re-assign to new value
- could use bang method by adding $!$ at the last of built-in function
### 6.3. Predicate Methods
- end with $?#

## 7. Enumerable Methods
### 7.1. Block vs multi-line block
- Parameter: $|$ ... $|$ be put after the opening of block
- Block: use $\{$ ... $\}$
- Multi-line block: use $do$ ... $end$
- lambda: use $lambda$ or $ -> (...) $ care about input
- proc: use $Proc.new$ or $proc$ doesnt care about input, map $nil$ if missing