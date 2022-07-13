import pytest

from pybov import errors
from pybov import types


def test_header(b3_demo_data):
    header = b3_demo_data.split('\n')[0].replace('\n', '')
    b3_header = types.Header.from_str(header)

    assert b3_header.regtype == '00'
    assert b3_header.fname == 'COTAHIST.2003'
    assert b3_header.source_type == 'BOVESPA'
    assert b3_header.date == '20040531'
    assert repr(b3_header) == header


def test_footer(b3_demo_data):
    footer = b3_demo_data.split('\n')[-2].replace('\n', '')
    b3_footer = types.Footer.from_str(footer)

    assert b3_footer.regtype == '99'
    assert b3_footer.fname == 'COTAHIST.2003'
    assert b3_footer.source_type == 'BOVESPA'
    assert b3_footer.date == '20040531'
    assert b3_footer.total_records == 553
    assert repr(b3_footer) == footer


def test_record(b3_demo_data):
    record = b3_demo_data.split('\n')[10].replace('\n', '')
    b3_record = types.Record.from_str(record)

    assert b3_record.regtype == '01'
    assert b3_record.date == '20030212'
    assert b3_record.bdi == types.BDI('96')
    assert b3_record.ticker == 'TBLE3F'
    assert b3_record.value_type == types.ValueType('020')
    assert b3_record.company_short_name == 'TRACTEBEL'
    assert b3_record.category == [types.Category.from_str('ON'), types.Category.from_str('*')]
    assert b3_record.currency == 'R$'
    assert b3_record.price_opening == 345
    assert b3_record.price_high == 345
    assert b3_record.price_low == 320
    assert b3_record.price_average == 320
    assert b3_record.price_closing == 320
    assert b3_record.price_bid_best == 320
    assert b3_record.price_ask_best == 338
    assert b3_record.deals == 7
    assert b3_record.transactions == 48943
    assert b3_record.volume == 15660
    assert b3_record.price_strike == 0
    assert b3_record.price_correction_reference == types.PriceCorrectionReference('0')
    assert b3_record.expiration_date == 99991231
    assert b3_record.batch == 1000
    assert b3_record.price_strike_points == 0
    assert b3_record.isin_id == 'BRTBLEACNOR2'
    assert b3_record.dismes == '102'
    assert repr(b3_record) == record


def test_bdi_ok():
    b3_bdi = types.BDI.from_str('50')

    assert b3_bdi == types.BDI('50')
    assert str(b3_bdi) == 'Auction'


def test_bdi_error():
    with pytest.raises(errors.PyBovError) as e:
        types.BDI.from_str('712')

    assert e.value.code == 1
    assert e.value.message == 'Unable to find value "712"'


def test_category_ok():
    b3_category = types.Category.from_str('BNS B/A')

    assert b3_category == types.Category('BNS B/A')
    assert str(b3_category) == 'BNSBA'


def test_category_error():
    with pytest.raises(errors.PyBovError) as e:
        types.Category.from_str('BNS XPTO')

    assert e.value.code == 1
    assert e.value.message == 'Unable to find value "BNS XPTO"'


def test_priceref_ok():
    b3_priceref = types.PriceCorrectionReference.from_str('1')

    assert b3_priceref == types.PriceCorrectionReference('1')
    assert str(b3_priceref) == 'USD'


def test_priceref_error():
    with pytest.raises(errors.PyBovError) as e:
        types.PriceCorrectionReference.from_str('10')

    assert e.value.code == 1
    assert e.value.message == 'Unable to find value "10"'


def test_value_ok():
    b3_value = types.ValueType.from_str('010')

    assert b3_value == types.ValueType('010')
    assert str(b3_value) == 'CASH'


def test_value_error():
    with pytest.raises(errors.PyBovError) as e:
        types.ValueType.from_str('99')

    assert e.value.code == 1
    assert e.value.message == 'Unable to find value "99"'
