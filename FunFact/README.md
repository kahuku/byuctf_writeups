# BYUCTF Winter 2022 - Fun Fact (Medium) Writeup
* Type - Reverse Engineering
* Name - Fun Facct
* Points - 241

## Description
```
This challenge will help you to learn more about reverse engineering Python code. But if not, you can learn more about sea creatures!!
Flag format - byuctf{message}
```

## Solution
I start by taking a look at the obfuscated code. It's only three lines long.
```
import base64
string = "aW1wb3J0IHJhbmRvbSwgc3RyaW5nCiAgICAKZGVmIG9wdGlvbl9vbmUoKToKICAgIHByaW50KCJcbkp1c3Qga2lkZGluZywgaXQncyBub3QgdGhhdCBlYXN5XG4iKQogICAgbWFpbigpCiAgICAKZGVmIG9wdGlvbl90d28oKToKICAgIHJhbmRvbV9mYWN0cyA9IFsiRWFjaCBhcm0gb2YgYW4gb2N0b3B1cyBoYXMgaXRzIG93biBuZXJ2b3VzIHN5c3RlbSIsICJDb21iIGplbGxpZXMgYXJlIHRyYW5zcGFyZW50LCBiaW9sdW1pbmVzY2VudCwgYW5kIGxpdmUgaW4gdGhlIHR3aWxpZ2h0IHpvbmUiLCAiU3RhciBmaXNoIGFyZSBlY2hpbm9kZXJtcyBhbmQgZG9uJ3QgaGF2ZSBicmFpbnMiLCAiR3JlZW5sYW5kIHNoYXJrcyBhcmUgdGhlIHNsb3dlc3Qgc2hhcmtzIGFuZCBkZXZlbG9wIHBhcmFzaXRlcyBpbiB0aGVpciBleWVzIiwgIldoYWxlIHNoYXJrcyBhcmUgdGhlIGxhcmdlc3Qgc2hhcmtzLCB3aXRoIG1vdXRocyB1cCB0byAxNSBmZWV0IHdpZGUgYnV0IGFyZSBvbmx5IGZpbHRlciBmZWVkZXJzIiwgIkJhc2tpbmcgc2hhcmtzIGFyZSBhbHNvIHNoYXJrcyB3aXRoIHdpZGUgbW91dGhzIHRoYXQgYXJlIG9ubHkgZmlsdGVyIGZlZWRlcnMiLCAiVGhlcmUgYXJlIGVsZWN0cmljIHN0aW5ncmF5cyB0aGF0IGFyZSBhYmxlIHRvIHNlbmQgZWxlY3RyaWMgc2hvY2tzIHRvIHByZWRhdG9ycyBpbiBvcmRlciB0byBzdHVuIHRoZW0gYW5kIGVzY2FwZSIsICJUaGUgcGFjZmljIG9jdG9wdXMgaXMgdGhlIGxhcmdlc3Qgb2N0b3B1cyIsICJUaGVyZSBhcmUgOCBzcGVjaWVzIG9mIHNlYSB0dXJ0bGVzLCBhbHRob3VnaCBpdCBpcyBkZWJhdGVkIHRoYXQgdGhlcmUgYXJlIG9ubHkgICBMZWF0aGVyYmFjayAgT2xpdmUgUmlkZGxleSAgS2VtcCBSaWRkbGV5ICBIYXdrc2JpbGwgIExvZ2dlcmhlYWQgIEZsYXRiYWNrICBHcmVlbiAgQmxhY2sgKGFsdG91Z2ggZGViYXRlZCB0byBiZSB0aGUgc2FtZSBzcGVjaWVzIGFzIEdyZWVuKSIsICJUaGUgbGVhdGhlcmJhY2sgc2VhIHR1cnRsZSBpcyB0aGUgbGFyZ2VzdCBzcGVjaWVzIG9mIHNlYSB0dXJ0bGUsIGdyb3dpbmcgdXAgdG8gOSBmZWV0IGxvbmciLCAiVGhlIGdlbmRlciBvZiBzZWEgdHVydGxlcyBpcyBkZXBlbmRlbnQgb24gdGhlIHRlbXBlcmF0dXJlIHdoZXJlIHRoZSBlZ2dzIHdlcmUgbGFpZCIsICJTZWEgdHVydGxlcyBhcmUgTk9UIHN0cmljdGx5IGhlcmJpdm9yZXMgYnV0IGFsc28gZWF0IGplbGx5ZmlzaCIsICJTZWEgdHVydGxlcyBuZWVkIHRvIGJyZWF0aCBhaXIuIElmIHRoZXkgYXJlIHNjYXJlZCBvZmYgdGhlIGJlYWNoIGJ5IGh1bWFucyB0aGV5IGNvdWxkIHBvdGVudGlhbGx5IHN3aW0gb3V0IHRvbyBmYXIgYW5kIHRoZW4gZHJvd24gYmVmb3JlIG1ha2luZyBpdCBiYWNrIHRvIGxhbmQiLCAiSGF3a3NiaWxsIHNlYSB0dXJ0bGVzIGFyZSBodW50ZWQgZG93biBmb3IgdGhlaXIgc2hlbGxzIiwgIkJybyBob3cgYXJlIGplbGx5ZmlzaCBhbmltYWxzPz8gVGhleSBoYXZlIG5vIGJyYWlucyEgU2FtZSB3aXRoIHNlYSBzdGFycyIsICJTZWEgc3RhcnMgd2lsbCBraWxsIHRoZWlyIHByYXkgd2l0aCBhY2lkIGFuZCB0aGVuIHR1cm4gdGhlaXIgc3RvbWFjaHMgaW5zaWRlIG91dCB0byBlYXQiLCAiU2hhcmtzIGNhbiBhbHNvIHR1cm4gdGhlaXIgc3RvbWFjaHMgaW5zaWRlIG91dCB0byByZWdlcmdpdGF0ZSBmb29kIiwgIlRpZ2VyIHNoYXJrcyBoYXZlIGluY3JlZGlibHkgc2hhcnAgdGVldGggdGhhdCBjYW4gYml0ZSB0aHJvdWdoIG1ldGFsIiwgIlRpZ2VyIHNoYXJrcyBhcmUgY2FsbGVkIHRoZSBnYXJiYWdlIGd1dCBvZiB0aGUgc2VhIGFuZCB0aGVyZSBhcmUgYmVlbiBsaWNlbnNlIHBsYWNlcywgdGlyZXMsIGFuZCBvdGhlciB3ZWlyZCB0aGluZ3MgZm91bmQgaW4gdGhlaXIgc3RvbWFjaHMiLCAiU29tZSBzaGFya3MgZG9uJ3QgaGF2ZSB0byBiZSBjb25zdGFudGx5IG1vdmluZyBpbiBvcmRlciB0byBicmVhdGguIEJ1Y2NhbCBwdW1waW5nIHZzIG9ibGlnYXRlIHJhbSB2ZW50aWxhdGlvbiIsICJUaGUgb25seSBib25lcyBzaGFya3MgaGF2ZSBhcmUgdGhlaXIgamF3cy4gVGhlaXIgc2tlbGV0YWwgc3RydWN0dXJlIGlzIG1hZGUgb3V0IG9mIGNhcnRpbGFnZSIsICJUaGUgb25seSBib25lcyBhbiBvY3RvcHVzIGhhcyBpcyB0aGVpciBiZWFrLCB3aGljaCBpcyBpbiB0aGUgY2VudGVyIG9mIHRoZWlyIGFybXMiLCAiQW4gb2N0b3B1cyBjYW4gZml0IHRocm91Z2ggYW55dGhpbmcgdGhhdCB0aGVpciBiZWFrIGNhbiBmaXQgdGhyb3VnaCIsICJIYWdmaXNoIGFyZSBzbyB3ZWlyZCBndXlzLiBUaGV5IHByb2R1Y2UgYSBsb3Qgb2Ygc2xpbWUiLCAiT2N0b3B1c2VzIGFyZSBrbm93biB0byBiZSB2ZXJ5IHNtYXJ0IGFuZCB2ZXJ5IGN1cmlvdXMgY3JlYXR1cmVzLiBUaGV5IHdpbGwgaW52ZXN0aWdhdGUgYW5kIHBsYXkgd2l0aCBzY3ViYSBkaXZlcnMiLCAiVGhlIHNtYWxsZXN0IHNoYXJrIGlzIHNvbWUgdHlwZSBvZiBsYW50ZXJuIHNoYXJrIChmb3Jnb3QgdGhlIGV4YWN0IG5hbWUpIiwgIkxlbW9uIHNoYXJrcyBhcmUgbmFtZWQgc3VjaCBiZWNhdXNlIHRoZWlyIHNraW4gZmVlbHMgbGlrZSBsZW1vbiByaW5kcyIsICJDb29raWUgY3V0dGVyIHNoYXJrcyBhcmUgbmFtZWQgc3VjaCBiZWNhdXNlIHRoZWlyIHRlZXRoIHRha2Ugb3V0IHNtYWxsLCBjaXJjdWxhciBjaHVua3MsIGtpbmQgb2YgbGlrZSBhIGNvb2tpZSBjdXR0ZXIiLCAiRGVlcCBzZWEgYW5nbGVyIGZpc2g6IHRoZSBmZW1hbGUgaXMgbXVjaCwgbXVjaCBsYXJnZXIgdGhhbiB0aGUgbWFsZSIsICJJbiB0aGUgcGFzdCwgcGVvcGxlIGhhdmUgdHJpZWQgdG8gYWRkIGdyZWF0IHdoaXRlIHNoYXJrcyBpbnRvIGFxdWFyaXVtcy4gSG93ZXZlciwgdGhlIGdyZWF0IHdoaXRlcyB3b3VsZCBqdXN0IGRpZSBpZiB0aGV5IHdlcmUgcmVzdHJpY3RlZCB0byBzdWNoIGEgc21hbGwgc3BhY2UiLCAiVGhlIGxhcmdlc3QgamVsbHlmaXNoIGlzIGNhbGxlZCB0aGUgbGlvbnMgbWFuZSIsICJNb3N0IHZlbm9tb3VzIGplbGx5ZmlzaCBpcyB0aGUgYm94amVsbHlmaXNoIiwgIk1vc3QgdmVub21vdXMgb2N0b3B1cyBpcyB0aGUgYmx1ZS1yaW5nZWQgb2N0b3B1cyIsICJNb3N0IHZlbmVtb3VzIHNlYSBzbmFpbCBpcyB0aGUgY29uZSBzbmFpbCIsICJTYW5kIGRvbGxhcnMgYXJlIGFjdHVhbGx5IHNlYSB1cmNoaW5zIiwgIlRoZSBjcm93biBvZiB0aG9ybnMgaXMgYW4gZXh0cmVtZWx5IGludmFzaXZlIHNwZWNpZXMgb2Ygc2VhIHN0YXIiLCAiVGhlIHNldmVyZWQgbGltYnMgb2Ygc2VhIHN0YXJzIHdpbGwgZ3JvdyBpbnRvIGFub3RoZXIgc2VhIHN0YXIiLCAiUGVvcGxlIHdvdWxkIHRyeSB0byBraWxsIHRoZSBjcm93biBvZiB0aG9ybnMgYnkgc21hc2hpbmcgdGhlbSwgYnV0IHRoYXQgYmFja2ZpcmVkIGJlY2F1c2UgdGhlIHNldmVyZWQgbGltYnMganVzdCBiZWNhbWUgYW5vdGhlciBzZWEgc3RhciIsICJBcmNoZXIgZmlzaCB3aWxsIHNwaXQgb3V0IHdhdGVyIHRvIGtub2NrIGJ1Z3Mgb2ZmIG9mIHBsYW50cyBzbyB0aGF0IHRoZXkgY2FuIGVhdCB0aGVtIiwgIkJhYnkgc2hhcmtzIGFyZSBjYWxsZWQgcHVwcyIsICJaZWJyYSBzaGFya3MgYXJlIG1vcmUgY29tbW9ubHkga25vd24gYXMgbGVvcGFyZCBzaGFya3MgaW4gYW5kIGFyb3VuZCB0aGUgQW5kYW1hbiBTZWEsIGJ1dCB0aGlzIGlzIGNvbmZ1c2luZyBhcyB0aGVyZSBpcyBhbm90aGVyIHNwZWNpZXMgb2Ygc2hhcmsgY2FsbGVkIHRoZSBsZW9wYXJkIHNoYXJrIiwgIk9yY2FzIGFyZSB0aGUgbGFyZ2VzdCBtZW1iZXJzIG9mIHRoZSBkb2xwaGluIGZhbWlseSIsICJLaWxsZXIgd2hhbGVzIGFyZSB0aGUgbW9zdCB3aWRlbHkgZGlzdHJpYnV0ZWQgbWFtbWFscywgb3RoZXIgdGhhbiBodW1hbnMgYW5kIHBvc3NpYmx5IGJyb3duIHJhdHMsIGFjY29yZGluZyB0byBTZWFXb3JsZC4gVGhleSBsaXZlIGluIGV2ZXJ5IG9jZWFuIGFyb3VuZCB0aGUgd29ybGQgYW5kIGhhdmUgYWRhcHRlZCB0byBkaWZmZXJlbnQgY2xpbWF0ZXMsIGZyb20gdGhlIHdhcm0gd2F0ZXJzIG5lYXIgdGhlIGVxdWF0b3IgdG8gdGhlIGljeSB3YXRlcnMgb2YgdGhlIE5vcnRoIGFuZCBTb3V0aCBQb2xlIHJlZ2lvbnMiXQogICAgcmFuZG9tX251bWJlciA9IHJhbmRvbS5yYW5kaW50KDAsIDQyKQogICAgcHJpbnQoIlxuIiwgcmFuZG9tX2ZhY3RzW3JhbmRvbV9udW1iZXJdLCAiXG4iKQogICAgbWFpbigpCgpkZWYgb3B0aW9uX3RocmVlKCk6CiAgICB1c2VyX2lucHV0ID0gaW5wdXQoIlxuRmxhZz4gIikKICAKICAgIHJhbmRvbV9hcnJheSA9IHhvcigiU25vd2ZsYWtlIGVlbHMgaGF2ZSB0d28gc2V0cyBvZiBqYXdzIiwgInByZXR0eSBjcmF6eSwgaHVoPyIpIAogICAgb3RoZXJfcmFuZG9tX2FycmF5ID0gbGlzdChzdHJpbmcucHJpbnRhYmxlKQogICAga2V5ID0gb3RoZXJfcmFuZG9tX2FycmF5W3JhbmRvbV9hcnJheVswXSArIHJhbmRvbV9hcnJheVs4XV0KICAgIAogICAgZW5jcnlwdGVkID0gIiIuam9pbihbY2hyKG9yZCh4KSBeIG9yZChrZXkpKSBmb3IgeCBpbiB1c2VyX2lucHV0XSkKICAgIHByaW50KCJlbmNyeXB0ZWQ6ICIsIGVuY3J5cHRlZCkKCiAgICBpZihlbmNyeXB0ZWQgPT0gJ2clNGMkemMlZHo0Z2c7Jyk6CiAgICAgICAgcHJpbnQoIlN1Y2Nlc3MhIikKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoIlxuVHJ5IGFnYWluIikKICAgICAgICBvcHRpb25fdGhyZWUoKQoKZGVmIHhvcihhLCBiKToKICAgIGtleSA9IFtdCiAgICBpID0gMAogICAgd2hpbGUgaSA8IGxlbihhKToKICAgICAgICBrZXkuYXBwZW5kKG9yZChhW2kgJSBsZW4oYSldKSBeIG9yZCgoYltpICUgbGVuKGIpXSkpKQogICAgICAgIGkgPSBpKzEKICAgIHJldHVybiBrZXkKCmRlZiBtYWluKCk6CiAgICBwcmludCgiRW50ZXIgMSB0byBwcmludCB0aGUgZmxhZyIpCiAgICBwcmludCgiRW50ZXIgMiBmb3IgYSBmdW4gZmFjdCBhYm91dCBvY2VhbiBjcmVhdHVyZXMiKQogICAgcHJpbnQoIkVudGVyIDMgdG8gY29udGludWUiKQoKICAgIHVzZXJfaW5wdXQgPSBpbnB1dCgiSW5wdXQ+ICIpCiAgICAKICAgIGlmKHVzZXJfaW5wdXQgPT0gJzEnKToKICAgICAgICBvcHRpb25fb25lKCkKICAgIGVsaWYodXNlcl9pbnB1dCA9PSAnMicpOgogICAgICAgIG9wdGlvbl90d28oKQogICAgZWxpZih1c2VyX2lucHV0ID09ICczJyk6CiAgICAgICAgb3B0aW9uX3RocmVlKCkKICAgIGVsc2U6CiAgICAgICAgcHJpbnQoIkludmFsaWQgb3B0aW9uIikKICAgICAgICAKbWFpbigp"
exec(base64.b64decode(string))
```

The last line gives us the most information. `exec` just executes a Python command. What's being passed in tells us how the code was obfuscated though. `base64.b64decode(string)` takes the variable string and decodes its base64 encryption. So really all this obfuscated code is doing is running a single Python program that is just currently hidden from us. Now, it's time to decode the string. Pasting that string into <www.base64decode.com> gives us the decoded version. It looks to be a perfectly normal Python program. Thankfully it wasn't obfuscated further. I pasted that code into a new Python file and ran it on my machine. We're met with this output
```
Enter 1 to print the flag
Enter 2 for a fun fact about ocean creatures
Enter 3 to continue
Input> 
```

Before even looking at the code, I try some different  to see how the program handles invalid user input. I input `-1`, `0`, `333`, and `100000000000000000` and each time, the program terminates with the output `Invalid option`. So it looks like breaking the program through its input probably isn't the correct approach. Since we do have the source code, the next step is to start looking through that. I always start with the base of the program
```def main():
    print("Enter 1 to print the flag")
    print("Enter 2 for a fun fact about ocean creatures")
    print("Enter 3 to continue")

    user_input = input("Input> ")
    
    if(user_input == '1'):
        option_one()
    elif(user_input == '2'):
        option_two()
    elif(user_input == '3'):
        option_three()
    else:
        print("Invalid option")
        
main()
```

This is where the program starts. It calls main, which prompts the user for input and then calls respective functions depending on the input. Nothing too special happening here.

```
def option_one():
    print("\nJust kidding, it's not that easy\n")
    main()
    
def option_two():
    random_facts = ["Each arm of an octopus has its own nervous system", "Comb jellies are transparent, bioluminescent, and live in the twilight zone", "Star fish are echinoderms and don't have brains", "Greenland sharks are the slowest sharks and develop parasites in their eyes", "Whale sharks are the largest sharks, with mouths up to 15 feet wide but are only filter feeders", "Basking sharks are also sharks with wide mouths that are only filter feeders", "There are electric stingrays that are able to send electric shocks to predators in order to stun them and escape", "The pacfic octopus is the largest octopus", "There are 8 species of sea turtles, although it is debated that there are only   Leatherback  Olive Riddley  Kemp Riddley  Hawksbill  Loggerhead  Flatback  Green  Black (altough debated to be the same species as Green)", "The leatherback sea turtle is the largest species of sea turtle, growing up to 9 feet long", "The gender of sea turtles is dependent on the temperature where the eggs were laid", "Sea turtles are NOT strictly herbivores but also eat jellyfish", "Sea turtles need to breath air. If they are scared off the beach by humans they could potentially swim out too far and then drown before making it back to land", "Hawksbill sea turtles are hunted down for their shells", "Bro how are jellyfish animals?? They have no brains! Same with sea stars", "Sea stars will kill their pray with acid and then turn their stomachs inside out to eat", "Sharks can also turn their stomachs inside out to regergitate food", "Tiger sharks have incredibly sharp teeth that can bite through metal", "Tiger sharks are called the garbage gut of the sea and there are been license places, tires, and other weird things found in their stomachs", "Some sharks don't have to be constantly moving in order to breath. Buccal pumping vs obligate ram ventilation", "The only bones sharks have are their jaws. Their skeletal structure is made out of cartilage", "The only bones an octopus has is their beak, which is in the center of their arms", "An octopus can fit through anything that their beak can fit through", "Hagfish are so weird guys. They produce a lot of slime", "Octopuses are known to be very smart and very curious creatures. They will investigate and play with scuba divers", "The smallest shark is some type of lantern shark (forgot the exact name)", "Lemon sharks are named such because their skin feels like lemon rinds", "Cookie cutter sharks are named such because their teeth take out small, circular chunks, kind of like a cookie cutter", "Deep sea angler fish: the female is much, much larger than the male", "In the past, people have tried to add great white sharks into aquariums. However, the great whites would just die if they were restricted to such a small space", "The largest jellyfish is called the lions mane", "Most venomous jellyfish is the boxjellyfish", "Most venomous octopus is the blue-ringed octopus", "Most venemous sea snail is the cone snail", "Sand dollars are actually sea urchins", "The crown of thorns is an extremely invasive species of sea star", "The severed limbs of sea stars will grow into another sea star", "People would try to kill the crown of thorns by smashing them, but that backfired because the severed limbs just became another sea star", "Archer fish will spit out water to knock bugs off of plants so that they can eat them", "Baby sharks are called pups", "Zebra sharks are more commonly known as leopard sharks in and around the Andaman Sea, but this is confusing as there is another species of shark called the leopard shark", "Orcas are the largest members of the dolphin family", "Killer whales are the most widely distributed mammals, other than humans and possibly brown rats, according to SeaWorld. They live in every ocean around the world and have adapted to different climates, from the warm waters near the equator to the icy waters of the North and South Pole regions"]
    random_number = random.randint(0, 42)
    print("\n", random_facts[random_number], "\n")
    main()
```
Nothing too important is happening here either. Option one just tells us that it won't just give us the flag. Option two prints a random sea creature fact. Both of them finish by calling `main()` again. So, it looks like option 3 is the code we care about

```
def option_three():
    user_input = input("\nFlag> ")
  
    random_array = xor("Snowflake eels have two sets of jaws", "pretty crazy, huh?") 
    other_random_array = list(string.printable)
    key = other_random_array[random_array[0] + random_array[8]]
    
    encrypted = "".join([chr(ord(x) ^ ord(key)) for x in user_input])
    print("encrypted: ", encrypted)

    if(encrypted == 'g%4c$zc%dz4gg;'):
        print("Success!")
    else:
        print("\nTry again")
        option_three()

def xor(a, b):
    key = []
    i = 0
    while i < len(a):
        key.append(ord(a[i % len(a)]) ^ ord((b[i % len(b)])))
        i = i+1
    return key
```
Option 3 starts by prompting the user for input. Then it calls a custom `xor` function on two hardcoded strings. That's great news for us. Since the strings are hardcoded in, we know that `random_array` will be initialized to the same value every time, regardless of the user's input. That allows us to simplify our code. It looks like `random_array` is only used two lines later, where the values at two hardcoded indexes are added together. Then, key is set to the value of `other_random_array` at that resulting index. `other_random_array` is just the following printable characters made into a list
```
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ 
```
So at this point, we can confirm that `key` will be the same value every time we run this code. So, I just added a `print(key)` after it's initialized and ran the code with random input. `W` is printed to the terminal. So now that we know what `key` is, it's fairly straightforward to reverse engineer the next few lines. It looks like the encrypted version of the user input will be printed, and if it's equal to the string `g%4c$zc%dz4gg;`, then that will be the correct flag. So basically, all we need to do is break down the line that assigns the value of `encrypted` and write some code to revese the process. `ord` returns the unicode code of a given character. So, that line first binary xors the unicode codes of the first character in the user's input with the caracter W. Then, it converts that xor-ed unicode back into a character. It repeates this for every character in user input using list comprehension, and then joins the result of that operation with the empty string to turn the result into a single string. So, all weneed to do is write code that does the inverse of this to the string `g%4c$zc%dz4gg;` to tell us what we need to enter to get the flag. There's definitely a more succint way to write this code, but I wanted to test my coce incrementally, so I wrote it in a way that may have not been the most efficient or elegant. Here's what I came up with

```
key = 'W'
encrypted = "g%4c$zc%dz4gg;"

s = []
for char in encrypted:
    s.append(ord(char))

l = []
for num in s:
    l.append(num ^ ord("W"))

s = ''
for num in l:
    char = chr(num)
    s += char
print(s)
```
We start by taking the unicode equivalent of every character in the encrypted string and adding that to a list. Then, for each unicode character in that list, I took the bitwise xor of that character with 'W' and added that result to a new list. Then finally, I converted each unicode character in that list back into a character and appended it to an empty string which I printed at the end. Running that code gives us the correct flag
```
byuctf{0rc4s-4r3-c00l}
```

## Real World Application
This problem taught me so many skills. First, was how to decode base64. Once I did that, I had some code that I had to reverse engineer. Being able to read and understand someone else's code is a talent in and of itself. It took a methodical and very step-by-step approach to determine how the `key` variable was being assigned. Once we were able to find out that key was just a static character that they tried to obfuscate, we were able to start breaking down the encryption method line by line. After I understood every single thing in that line, I was able to basically find the inverse of every function the code used, put them together in the reverse order, and used that to generate the input that the code was looking for. This is an extremely important skill to have. Interpreting someone else's code and genuinely understanding it is difficult, but once you're able to do that, you can figure out how to write code to basically undo everything the original code does, which is a very common challenge for reverse engineers.
