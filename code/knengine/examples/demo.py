
parse_tree = \
  ('knStats',
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'T'),
        ('formParams',
          ('kn_id', 'n'),
          ('kn_id', 'x')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '2'),
            ('opEq',
              ('kn_id', 'n'),
              ('kn_num', '0')
            ),
            ('condTerm',
              ('kn_id', 'x'),
              ('opEq',
                ('kn_id', 'n'),
                ('kn_num', '1')
              ),
              ('bMinus',
                ('opMult',
                  ('kn_id', 'x'),
                  ('actFunTerm',
                    ('kn_id', 'T'),
                    ('actParams',
                      ('bMinus',
                        ('kn_id', 'n'),
                        ('kn_num', '1')
                      ),
                      ('kn_id', 'x')
                    )
                  )
                ),
                ('actFunTerm',
                  ('kn_id', 'T'),
                  ('actParams',
                    ('bMinus',
                      ('kn_id', 'n'),
                      ('kn_num', '2')
                    ),
                    ('kn_id', 'x')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('varStat',
      ('knVars',
        ('kn_id', 'x')
      )
    ),
    ('checkStat',
      ('kn_id', 'test1'),
      ('actFunTerm',
        ('kn_id', 'T'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_id', 'x')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'test2'),
      ('actFunTerm',
        ('kn_id', 'T'),
        ('actParams',
          ('kn_num', '2'),
          ('opMult',
            ('kn_num', 'im'),
            ('kn_id', 'x')
          )
        )
      )
    )
  )

import kn_lib

check_list = []



def T(n, x):
    return 2 if kn_lib.opEq(n, 0) else x if kn_lib.opEq(n, 1) else kn_lib.bMinus(kn_lib.opMult(x, T(kn_lib.bMinus(n, 1), x)), T(kn_lib.bMinus(n, 2), x))

x = kn_lib.make_vars('x')


check_list.append(('test1', kn_lib.get_tex(T(2, x))))


check_list.append(('test2', kn_lib.get_tex(T(2, kn_lib.opMult(kn_lib.im, x)))))


check_str = ''

for check_pair in check_list:
    check_name, check_term = check_pair
    check_str += (
            check_name + ' = ' '\n\t'
            '$$ ' + check_term + ' $$'
            '\n\n'
        )

kn_lib.write_tex(check_str, r'examples/demo.tex')
