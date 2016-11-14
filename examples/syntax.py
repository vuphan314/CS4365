import kn_lib

check_list = []




check_list.append(('imaginaryUnitSquared', kn_lib.sp_tex((kn_lib.opExp(kn_lib.im, 2) if kn_lib.opOr(kn_lib.true, kn_lib.opNot(kn_lib.false)) else 1))))

def c1():
    return 1

def f1(x):
    return kn_lib.opExp(x, kn_lib.uMinus(2))

x = kn_lib.make_vars('x')


check_list.append(('f1x', kn_lib.sp_tex(f1(x))))

def f3(x, y):
    z1 = kn_lib.opDiv(1, x)
    z2 = (kn_lib.opDiv(x, y) if kn_lib.opEq(f1(kn_lib.opMod(x, y)), kn_lib.opDiv(5, 2)) else (1 if kn_lib.opEq(c1(), 3) else z1))
    return (kn_lib.opMod(z1, z2) if kn_lib.opEq(z1, 4) else (3 if kn_lib.false else kn_lib.opExp(kn_lib.im, 3)))

y, z = kn_lib.make_vars('y, z')


check_list.append(('t1', kn_lib.sp_tex((kn_lib.opPlus(kn_lib.opMod(y, z), f3(kn_lib.opMod(y, z), kn_lib.opPlus(kn_lib.uMinus(x), 2))) if kn_lib.true else 0))))


kn_lib.write_tex_file(check_list, r'../examples/syntax.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('checkStat',
      ('kn_id', 'imaginaryUnitSquared'),
      ('condTerm',
        ('opExp',
          ('kn_num', 'im'),
          ('kn_num', '2')
        ),
        ('opOr',
          ('key_truth', 'true'),
          ('opNot',
            ('key_truth', 'false')
          )
        ),
        ('kn_num', '1')
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'c1')
      ),
      ('defBody',
        ('retCl',
          ('kn_num', '1')
        )
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'f1'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('defBody',
        ('retCl',
          ('opExp',
            ('kn_id', 'x'),
            ('uMinus',
              ('kn_num', '2')
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
      ('kn_id', 'f1x'),
      ('actFunTerm',
        ('kn_id', 'f1'),
        ('actParams',
          ('kn_id', 'x')
        )
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'f3'),
        ('formParams',
          ('kn_id', 'x'),
          ('kn_id', 'y')
        )
      ),
      ('defBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'z1'),
            ('opDiv',
              ('kn_num', '1'),
              ('kn_id', 'x')
            )
          ),
          ('letCl',
            ('kn_id', 'z2'),
            ('condTerm',
              ('opDiv',
                ('kn_id', 'x'),
                ('kn_id', 'y')
              ),
              ('opEq',
                ('actFunTerm',
                  ('kn_id', 'f1'),
                  ('actParams',
                    ('opMod',
                      ('kn_id', 'x'),
                      ('kn_id', 'y')
                    )
                  )
                ),
                ('opDiv',
                  ('kn_num', '5'),
                  ('kn_num', '2')
                )
              ),
              ('condTerm',
                ('kn_num', '1'),
                ('opEq',
                  ('actFunTerm',
                    ('kn_id', 'c1')
                  ),
                  ('kn_num', '3')
                ),
                ('kn_id', 'z1')
              )
            )
          )
        ),
        ('retCl',
          ('condTerm',
            ('opMod',
              ('kn_id', 'z1'),
              ('kn_id', 'z2')
            ),
            ('opEq',
              ('kn_id', 'z1'),
              ('kn_num', '4')
            ),
            ('condTerm',
              ('kn_num', '3'),
              ('key_truth', 'false'),
              ('opExp',
                ('kn_num', 'im'),
                ('kn_num', '3')
              )
            )
          )
        )
      )
    ),
    ('varStat',
      ('knVars',
        ('kn_id', 'y'),
        ('kn_id', 'z')
      )
    ),
    ('checkStat',
      ('kn_id', 't1'),
      ('condTerm',
        ('opPlus',
          ('opMod',
            ('kn_id', 'y'),
            ('kn_id', 'z')
          ),
          ('actFunTerm',
            ('kn_id', 'f3'),
            ('actParams',
              ('opMod',
                ('kn_id', 'y'),
                ('kn_id', 'z')
              ),
              ('opPlus',
                ('uMinus',
                  ('kn_id', 'x')
                ),
                ('kn_num', '2')
              )
            )
          )
        ),
        ('key_truth', 'true'),
        ('kn_num', '0')
      )
    )
  )

lexing_sequence = [('key_check', 'check'), ('kn_id', 'imaginaryUnitSquared'), ('key_pri', 'print'), ('kn_num', 'im'), ('op_exp', '^'), ('kn_num', '2'), ('key_if', 'if'), ('key_truth', 'true'), ('op_or', 'or'), ('op_not', 'not'), ('key_truth', 'false'), ('key_else', 'else'), ('kn_num', '1'), ('key_def', 'define'), ('kn_id', 'c1'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '1'), ('key_def', 'define'), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'x'), ('op_exp', '^'), ('op_minus', '-'), ('kn_num', '2'), ('key_var', 'vary'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'f1x'), ('key_pri', 'print'), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_def', 'define'), ('kn_id', 'f3'), ('l_paren', '('), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'z1'), ('key_be', 'be'), ('kn_num', '1'), ('op_div', '/'), ('kn_id', 'x'), ('key_let', 'let'), ('kn_id', 'z2'), ('key_be', 'be'), ('kn_id', 'x'), ('op_div', '/'), ('kn_id', 'y'), ('key_if', 'if'), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('op_mod', '%'), ('kn_id', 'y'), ('r_paren', ')'), ('op_eq', '='), ('kn_num', '5'), ('op_div', '/'), ('kn_num', '2'), ('key_else', 'else'), ('kn_num', '1'), ('key_if', 'if'), ('kn_id', 'c1'), ('l_paren', '('), ('r_paren', ')'), ('op_eq', '='), ('kn_num', '3'), ('key_else', 'else'), ('kn_id', 'z1'), ('key_ret', 'return'), ('kn_id', 'z1'), ('op_mod', '%'), ('kn_id', 'z2'), ('key_if', 'if'), ('kn_id', 'z1'), ('op_eq', '='), ('kn_num', '4'), ('key_else', 'else'), ('kn_num', '3'), ('key_if', 'if'), ('key_truth', 'false'), ('key_else', 'else'), ('kn_num', 'im'), ('op_exp', '^'), ('kn_num', '3'), ('key_var', 'vary'), ('kn_id', 'y'), ('kn_comma', ','), ('kn_id', 'z'), ('key_check', 'check'), ('kn_id', 't1'), ('key_pri', 'print'), ('kn_id', 'y'), ('op_mod', '%'), ('kn_id', 'z'), ('op_plus', '+'), ('kn_id', 'f3'), ('l_paren', '('), ('kn_id', 'y'), ('op_mod', '%'), ('kn_id', 'z'), ('kn_comma', ','), ('op_minus', '-'), ('kn_id', 'x'), ('op_plus', '+'), ('kn_num', '2'), ('r_paren', ')'), ('key_if', 'if'), ('key_truth', 'true'), ('key_else', 'else'), ('kn_num', '0')]