#!/usr/bin/env python

from base64 import b64decode

s="VGhpcyBvbmUgd2FzIGJhc2U2NC4gSXQncyBhIGxpdHRsZSBoYXJkZXIgdGhhbiB0aGUgcHJldmlvdXMgbWlzc2lvbi4gVGhlID09IG9wZXJhdG9ycyBnaXZlIGJhc2U2NCBhd2F5Lg=="

print b64decode(s)
