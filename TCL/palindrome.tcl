set flag 0
set l "abcba"
set stringlength [string length $l]
puts "$stringlength"
for {set i 0} {$i < [string length $l] } {incr i} {
    set first [string index $l $i]
    set second [string index $l end-$i]
    set result [string compare $first $second]
    puts "$result"
    if {$result !=0} { break } else { set flag 1}
    
} 

if {$flag == 1} {  puts "string is a palindrome" } else { puts "not" }