import kn_lib

check_list = []



t, x, y = kn_lib.make_vars('t, x, y')

def X(j):
    return (kn_lib.bMinus(kn_lib.uMinus(kn_lib.opExp(t, 2)), kn_lib.opExp(t, kn_lib.uMinus(2))) if kn_lib.opEq(j, 0) else (kn_lib.bMinus(kn_lib.opMult(kn_lib.uMinus(kn_lib.opExp(t, 2)), kn_lib.opExp(x, 2)), kn_lib.opMult(kn_lib.opExp(t, 4), y)) if kn_lib.opEq(j, 1) else kn_lib.bMinus(kn_lib.bMinus(kn_lib.opMult(kn_lib.opMult(kn_lib.opExp(t, 2), y), X(kn_lib.bMinus(j, 1))), kn_lib.opMult(kn_lib.opExp(t, 4), X(kn_lib.bMinus(j, 2)))), kn_lib.opMult(kn_lib.opMult(2, kn_lib.opExp(t, 2)), kn_lib.opExp(x, 2)))))


check_list.append(('X0', kn_lib.sp_tex(X(0))))


check_list.append(('X1', kn_lib.sp_tex(X(1))))


check_list.append(('X2', kn_lib.sp_tex(X(2))))


check_list.append(('X3', kn_lib.sp_tex(X(3))))


check_list.append(('X4', kn_lib.sp_tex(X(4))))


check_list.append(('X5', kn_lib.sp_tex(X(5))))


kn_lib.write_tex_file(check_list, r'../examples/paperTwist.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 't'),
        ('kn_id', 'x'),
        ('kn_id', 'y')
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'X'),
        ('formParams',
          ('kn_id', 'j')
        )
      ),
      ('funBody',
        ('retCl',
          ('condTerm',
            ('bMinus',
              ('uMinus',
                ('opExp',
                  ('kn_id', 't'),
                  ('kn_num', '2')
                )
              ),
              ('opExp',
                ('kn_id', 't'),
                ('uMinus',
                  ('kn_num', '2')
                )
              )
            ),
            ('opEq',
              ('kn_id', 'j'),
              ('kn_num', '0')
            ),
            ('condTerm',
              ('bMinus',
                ('opMult',
                  ('uMinus',
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '2')
                    )
                  ),
                  ('opExp',
                    ('kn_id', 'x'),
                    ('kn_num', '2')
                  )
                ),
                ('opMult',
                  ('opExp',
                    ('kn_id', 't'),
                    ('kn_num', '4')
                  ),
                  ('kn_id', 'y')
                )
              ),
              ('opEq',
                ('kn_id', 'j'),
                ('kn_num', '1')
              ),
              ('bMinus',
                ('bMinus',
                  ('opMult',
                    ('opMult',
                      ('opExp',
                        ('kn_id', 't'),
                        ('kn_num', '2')
                      ),
                      ('kn_id', 'y')
                    ),
                    ('actFunExpr',
                      ('kn_id', 'X'),
                      ('actParams',
                        ('bMinus',
                          ('kn_id', 'j'),
                          ('kn_num', '1')
                        )
                      )
                    )
                  ),
                  ('opMult',
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '4')
                    ),
                    ('actFunExpr',
                      ('kn_id', 'X'),
                      ('actParams',
                        ('bMinus',
                          ('kn_id', 'j'),
                          ('kn_num', '2')
                        )
                      )
                    )
                  )
                ),
                ('opMult',
                  ('opMult',
                    ('kn_num', '2'),
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '2')
                    )
                  ),
                  ('opExp',
                    ('kn_id', 'x'),
                    ('kn_num', '2')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X0'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '0')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X1'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '1')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X2'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '2')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X3'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '3')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X4'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '4')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X5'),
      ('actFunExpr',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '5')
        )
      )
    )
  )

lexing_sequence = [('key_unknown', 'unknown'), ('kn_id', 't'), ('kn_comma', ','), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('key_fun', 'function'), ('kn_id', 'X'), ('l_paren', '('), ('kn_id', 'j'), ('r_paren', ')'), ('key_ret', 'return'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_num', '2'), ('key_if', 'if'), ('kn_id', 'j'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'y'), ('key_if', 'if'), ('kn_id', 'j'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'y'), ('op_mult', '*'), ('kn_id', 'X'), ('l_paren', '('), ('kn_id', 'j'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'X'), ('l_paren', '('), ('kn_id', 'j'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('op_minus', '-'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('key_check', 'check'), ('kn_id', 'X0'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '0'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X1'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '1'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X2'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '2'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X3'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '3'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X4'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '4'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X5'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '5'), ('r_paren', ')')]
