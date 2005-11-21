#!/usr/bin/env python
import utils

import unittest

from kiwi.ui.widgets.combobox import ComboBox

class TestComboBox(unittest.TestCase):
    def setUp(self):
        self.combo = ComboBox()

    def _prefill(self):
        self.combo.prefill((('Johan', 1981),
                            ('Lorenzo', 1979),
                            ('Christian', 1976)))
                           
    def testPrefill(self):
        self.combo.prefill(('foo', 'bar'))
        model = self.combo.get_model()
        self.assertEqual(tuple(model[0]), ('foo', None))
        self.assertEqual(tuple(model[1]), ('bar', None))
        
    def testPrefillWithData(self):
        self.combo.prefill((('foo', 42), ('bar', 138)))
        model = self.combo.get_model()
        self.assertEqual(tuple(model[0]), ('foo', 42))
        self.assertEqual(tuple(model[1]), ('bar', 138))
        self.combo.prefill([])
        self.assertEqual(len(self.combo.get_model()), 0)
        self.assertEqual(len(model), 0)
        self.assertEqual(len(self.combo), 0)

    def testSelectItemByPosition(self):
        self._prefill()
        self.combo.select_item_by_position(1)
        model = self.combo.get_model()
        iter = self.combo.get_active_iter()
        self.assertEqual(model.get_value(iter, 0), 'Lorenzo')
        self.assertEqual(model.get_value(iter, 1), 1979)
        self.assertRaises(KeyError, self.combo.select_item_by_label, 4)

    def testSelectItemByLabel(self):
        self._prefill()
        self.combo.select_item_by_label('Christian')
        model = self.combo.get_model()
        iter = self.combo.get_active_iter()
        rowNo = model.get_path(iter)[0]
        self.assertEqual(rowNo, 2)
        self.assertRaises(KeyError, self.combo.select_item_by_label, 'Salgado')

    def testSelectByData(self):
        self._prefill()
        self.combo.select_item_by_data(1976)
        model = self.combo.get_model()
        iter = self.combo.get_active_iter()
        rowNo = model.get_path(iter)[0]
        self.assertEqual(rowNo, 2)
        self.assertEqual(model.get_value(iter, 0), 'Christian')
        self.assertEqual(model.get_value(iter, 1), 1976)
        self.assertRaises(KeyError, self.combo.select_item_by_data, 1980)

    def testGetSelectedData(self):
        self._prefill()
        self.combo.select_item_by_position(0)
        self.assertEqual(self.combo.get_selected_data(), 1981)
        self.assertRaises(TypeError, 
                          self.combo.select_item_by_position, 'foobar')
        
    def testGetSelectedLabel(self):
        self._prefill()

    def testClear(self):
        self._prefill()
        self.combo.clear()
        self.assertEqual(map(list, self.combo.get_model()), [])
    
if __name__ == '__main__':
    unittest.main()
