•After f = methodcaller('name'), the call f(b) returns b.name().
•After f = methodcaller('name', 'foo', bar=1), the call f(b) returns b.name('foo', bar=1).


•After f = itemgetter(2), the call f(r) returns r[2].
•After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3]).

•After f = attrgetter('name'), the call f(b) returns b.name.
•After f = attrgetter('name', 'date'), the call f(b) returns (b.name, b.date).
•After f = attrgetter('name.first', 'name.last'), the call f(b) returns (b.name.first, b.name.last).

operator.length_hint(obj, default=0)
Return an estimated length for the object o. First try to return its actual length, then an estimate using object.__length_hint__(), and finally return the default value.
