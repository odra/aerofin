"""
This module contains all b3 data classes
which are used to represent b3 historical record data.
"""
from typing import Any, List
from enum import Enum
from dataclasses import dataclass, asdict

import canonicaljson  # type: ignore

from pybov import helpers, errors


#TODO: use proper typing
def as_json(model: Any) -> str:
    """
    Return a model in json string format.
    """
    parsed = asdict(model, dict_factory=asdict_enum_factory)

    return str(canonicaljson.encode_canonical_json(parsed).decode())


#TODO: use proper typing
def asdict_enum_factory(data: Any) -> Any:
    """
    Function used as dataclasses.asdict factory.

    It is used to make specific fields to be parseable as
    json string data.
    """
    def convert(obj: Any) -> Any:
        if isinstance(obj, Enum):
            return str(obj)
        return obj

    return dict((k, convert(v)) for k, v in data)


@dataclass
class Header:
    """
    Header record data class.
    """

    regtype: str
    fname: str
    source_type: str
    date: str

    @classmethod
    def from_str(cls, data: str) -> 'Header':
        """
        Deserializes a header string into a Header object.
        """
        return cls(
            data[0:2],
            data[2:15],
            data[15:23].strip(),
            data[23:31]
        )

    def __repr__(self) -> str:
        """
        Serializes the object data returning its original
        string representation.
        """
        return ''.join([
            self.regtype,
            self.fname,
            helpers.fill_str(self.source_type, 23 - 15),
            self.date,
            helpers.fill_str('', 214)
        ])


@dataclass
class Footer:
    """
    Footer record data class.
    """

    regtype: str
    fname: str
    source_type: str
    date: str
    total_records: int

    @classmethod
    def from_str(cls, data: str) -> 'Footer':
        """
        Deserializes a footer string into a Header object.
        """
        return cls(
            data[0:2],
            data[2:15],
            data[15:23].strip(),
            data[23:31],
            int(data[31:42])
        )

    def __repr__(self) -> str:
        """
        Serializes the object data returning its original
        string representation.
        """
        return ''.join([
            self.regtype,
            self.fname,
            helpers.fill_str(self.source_type, 23 - 15),
            self.date,
            helpers.fill_str(str(self.total_records),
                             42 - 31, char='0', order=-1),
            helpers.fill_str('', 203)
        ])


class BDI(Enum):
    """
    Enum that stores BDI codes.
    """

    Default: str = '02'
    B3Regulation: str = '05'
    Agreement: str = '06'
    ExtraJudicialRecovery: str = '07'
    JudicialRecovery: str = '08'
    RAET: str = '09'
    Rights: str = '10'
    Intervention: str = '11'
    REIT: str = '12'
    Debenture: str = '14'
    Liabilities: str = '18'
    Bonus: str = '22'
    Policies: str = '26'
    OptionCallExerciseIndex: str = '32'
    OptionPutExerciseIndex: str = '33'
    OptionCallExercise: str = '38'
    OptionPutExercise: str = '42'
    AuctionUnquoted: str = '46'
    AuctionPrivatization: str = '48'
    AuctionESRecoveryFund: str = '49'
    Auction: str = '50'
    AuctionFinor: str = '51'
    AuctionFinam: str = '52'
    AuctionFiset: str = '53'
    AuctionArrears: str = '54'
    JudicialPermit: str = '56'
    Other: str = '58'
    SwapShare: str = '60'
    Goal: str = '61'
    Term: str = '62'
    Debenture3Y: str = '66'
    Debenture3YP: str = '68'
    FutureContractGain: str = '70'
    Future: str = '71'
    OptionCallIndex: str = '74'
    OptionPutOption: str = '75'
    OptionCall: str = '78'
    OptionPut: str = '82'
    FixedIncoml: str = '83'
    FixedIncomeLegacy: str = '84'
    TermProspect: str = '90'
    Fractionary: str = '96'
    Sum: str = '99'

    @classmethod
    def from_str(cls, value: str) -> 'BDI':
        """
        Returns a new instance based on the provided value.

        Raises `errors.OTSError` in case an invalid value is used.
        """
        try:
            return cls(value)
        except ValueError:
            raise errors.PyBovError(f'Unable to find value "{value}"')

    def __str__(self) -> str:
        """
        Returns the instance name field.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Returns the instance value field.
        """
        return self.value


class Category(Enum):
    """
    Category enum.
    """

    BDR: str = 'BDR'
    BNS: str = 'BNS'
    BNSBA: str = 'BNS B/A'
    BNSORD: str = 'BNS ORD'
    BNSPA: str = 'BNS P/A'
    BNSPB: str = 'BNS P/B'
    BNSPC: str = 'BNS P/C'
    BNSPD: str = 'BNS P/D'
    BNSPE: str = 'BNS P/E'
    BNSPF: str = 'BNS P/F'
    BNSPG: str = 'BNS P/G'
    BNSPH: str = 'BNS P/H'
    BNSPRE: str = 'BNS PRE'
    CDA: str = 'CDA'
    CI: str = 'CI'
    CPA: str = 'CPA'
    CIATZ: str = 'CI ATZ'
    CIEA: str = 'CI EA'
    CIEBA: str = 'CI EBA'
    CIED: str = 'CI ED'
    CIER: str = 'CI ER'
    CIERA: str = 'CI ERA'
    CIERB: str = 'CI ERB'
    CIERS: str = 'CI ERS'
    CIES: str = 'CI ES'
    DIR: str = 'DIR'
    DIRDEB: str = 'DIR DEB'
    DIRORD: str = 'DIR ORD'
    DIRPA: str = 'DIR P/A'
    DIRPB: str = 'DIR P/B'
    DIRPC: str = 'DIR P/C'
    DIRPD: str = 'DIR P/D'
    DIRPE: str = 'DIR P/E'
    DIRPF: str = 'DIR P/F'
    DIRPG: str = 'DIR P/G'
    DIRPR: str = 'DIR P/R'
    DIRPRA: str = 'DIR PRA'
    DIRPRB: str = 'DIR PRB'
    DIRPRC: str = 'DIR PRC'
    DIRPRE: str = 'DIR PRE'
    FIDC: str = 'FIDC'
    LFT: str = 'LFT'
    M1REC: str = 'M1 REC'
    ON: str = 'ON'
    ONATZ: str = 'ON ATZ'
    ONEB: str = 'ON EB'
    ONED: str = 'ON ED'
    ONEDB: str = 'ON EDB'
    ONEDJ: str = 'ON EDJ'
    ONEDR: str = 'ON EDR'
    ONEG: str = 'ON EG'
    ONEJ: str = 'ON EJ'
    ONEJB: str = 'ON EJB'
    ONEJS: str = 'ON EJS'
    ONER: str = 'ON ER'
    ONERJ: str = 'ON ERJ'
    ONES: str = 'ON ES'
    ONP: str = 'ON P'
    ONREC: str = 'ON REC'
    ONALL: str = 'ON *'
    OR: str = 'OR'
    ORP: str = 'OR P'
    PCD: str = 'PCD'
    PN: str = 'PN'
    PNEB: str = 'PN EB'
    PNED: str = 'PN ED'
    PNEDB: str = 'PN EDB'
    PNEDJ: str = 'PN EDJ'
    PNEDR: str = 'PN EDR'
    PNEJ: str = 'PN EJ'
    PNEJB: str = 'PN EJB'
    PNEJS: str = 'PN EJS'
    PNES: str = 'PN ES'
    PNP: str = 'PN P'
    PNREC: str = 'PN REC'
    PNA: str = 'PNA'
    PNAEB: str = 'PN AEB'
    PNAEDR: str = 'PN AEDR'
    PNAEJ: str = 'PN AEJ'
    PNAES: str = 'PN AES'
    PNAP: str = 'PN AP'
    PNAREC: str = 'PNA REC'
    PNB: str = 'PNB'
    PNBEB: str = 'PNB EB'
    PNBEDR: str = 'PNB EDR'
    PNBEJ: str = 'PNB EJ'
    PNBES: str = 'PNB ES'
    PNBP: str = 'PNB P'
    PNBREC: str = 'PNB REC'
    PNC: str = 'PNC'
    PNCEB: str = 'PNC EB'
    PNCEDR: str = 'PNC EDR'
    PNCEJ: str = 'PNC EJ'
    PNCES: str = 'PNC ES'
    PNCP: str = 'PNC P'
    PNCREC: str = 'PNC REC'
    PND: str = 'PND'
    PNDEB: str = 'PND EB'
    PNDEDR: str = 'PND EDR'
    PNDEJ: str = 'PND EJ'
    PNDES: str = 'PND ES'
    PNDP: str = 'PND P'
    PNDREC: str = 'PND REC'
    PNE: str = 'PNE'
    PNEED: str = 'PNE ED'
    PNEP: str = 'PNE P'
    PNEREC: str = 'PNE REC'
    # The fields bellow were not in the docs
    ALL: str = '*'
    PNALL: str = 'PN *'
    PNN1: str = 'PN      N1'
    ONI02: str = 'ON *I02'
    ONNM: str = 'ON *    NM'
    ONN1: str = 'ON      N1'
    PNN2: str = 'PN      N2'
    PNAALL: str = 'PNA*'
    PNALLN1: str = 'PN *    N1'
    ONALLN1: str = 'ON *    N1'
    PNBALL: str = 'PNB*'
    DIRPREN1: str = 'DIR*PRE N1'

    @classmethod
    def from_str(cls, value: str) -> 'Category':
        """
        Returns a new instance based on the provided value.

        Raises `errors.OTSError` in case an invalid value is used.
        """
        try:
            return cls(value)
        except ValueError:
            raise errors.PyBovError(f'Unable to find value "{value}"')

    def __str__(self) -> str:
        """
        Returns the instance name field.
        """
        return self.name

    def __repr__(self) -> str:
        return self.value


class PriceCorrectionReference(Enum):
    """
    Price correction reference enum.
    """

    Null: str = '0'
    USD: str = '1'
    TJLP: str = '2'
    IGPM: str = '8'
    URV: str = '9'

    @classmethod
    def from_str(cls, value: str) -> 'PriceCorrectionReference':
        """
        Returns new instance based on the provided value.

        Raises `errors.OTSError` in case an invalid value is used.
        """
        try:
            return cls(value)
        except ValueError:
            raise errors.PyBovError(f'Unable to find value "{value}"')

    def __str__(self) -> str:
        """
        Returns the instance name field.
        """
        return self.name

    def __repr__(self) -> str:
        return self.value


class ValueType(Enum):
    """
    Value type enum.
    """

    CASH: str = '010'
    OPTION_CALL_EXERCISE: str = '012'
    OPTION_PUT_EXERCISE: str = '013'
    AUCTION: str = '017'
    FRACTIONARY: str = '020'
    TERM: str = '030'
    FUTURE_GAIN_RETENTION: str = '050'
    FUTURE_CONTINUOUS_RENTENTION: str = '060'
    OPTION_CALL: str = '070'
    OPTION_PUT: str = '080'

    @classmethod
    def from_str(cls, value: str) -> 'ValueType':
        """
        Returns a new instance based on the provided value.

        Raises `errors.OTSError` in case an invalid value is used.
        """
        try:
            return cls(value)
        except ValueError:
            raise errors.PyBovError(f'Unable to find value "{value}"')

    def __str__(self) -> str:
        """
        Returns the instance name field.
        """
        return self.name

    def __repr__(self) -> str:
        return self.value


@dataclass
class Record:
    """
    Record data class, represents a full record of a ticker in a day.

    This class glues all other enum together.
    """

    regtype: str
    date: str
    bdi: BDI
    ticker: str
    value_type: ValueType
    company_short_name: str
    category: List[Category]
    time_period: int
    currency: str
    price_opening: int
    price_high: int
    price_low: int
    price_average: int
    price_closing: int
    price_bid_best: int
    price_ask_best: int
    deals: int
    transactions: int
    volume: int
    price_strike: int
    price_correction_reference: PriceCorrectionReference
    expiration_date: int
    batch: int
    price_strike_points: int
    isin_id: str
    dismes: str

    @classmethod
    def from_str(cls, data: str) -> 'Record':
        """
        Deserializes a footer string into a Record object.
        """
        return cls(
            # regtype
            data[0:2],
            # data
            data[2:10],
            # bdi
            BDI.from_str(data[10:12].strip()),
            # ticker
            data[12:24].strip(),
            # value_type
            ValueType.from_str(data[24:27].strip()),
            # comany_short_name
            data[27:39].strip(),
            # category
            [Category.from_str(s) for s in data[39:49].strip().split(' ') if s],
            # time_period
            helpers.str2int(data[49:52]),
            # currency
            data[52:56].strip(),
            # price opening
            int(data[56:69]),
            # price_high
            int(data[69:82]),
            # price_low
            int(data[82:95]),
            # price_average
            int(data[95:108]),
            # price_closing
            int(data[108:121]),
            # price_bid_best
            int(data[121:134]),
            # price_ask_best
            int(data[134:147]),
            # deals
            int(data[147:152]),
            # transactions
            int(data[152:170]),
            # volume
            int(data[171:188]),
            # price_strike
            int(data[188:201]),
            # price_correction_reference
            PriceCorrectionReference.from_str(data[201:202].strip()),
            # expiration_date
            int(data[202:210]),
            # batch
            int(data[210:217]),
            # price_strike_points
            int(data[217:230]),
            # isin_id
            data[230:242],
            # dismes
            data[242:245]
        )

    def __repr__(self) -> str:
        """
        Serializes the object data returning its original
        string representation.
        """

        return ''.join([
            self.regtype,
            self.date,
            repr(self.bdi),
            helpers.fill_str(self.ticker, 12, char=' '),
            repr(self.value_type),
            helpers.fill_str(self.company_short_name, 12, char=' '),
            helpers.fill_str(' '.join([repr(c) for c in self.category]), 10, char= ' '),
            helpers.fill_str(str(self.time_period) if self.time_period > 0 else '', 3, char=' '),
            helpers.fill_str(self.currency, 4, char=' '),
            helpers.fill_str(str(self.price_opening), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_high), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_low), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_average), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_closing), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_bid_best), 13, char='0', order=-1),
            helpers.fill_str(str(self.price_ask_best), 13, char='0', order=-1),
            helpers.fill_str(str(self.deals), 5, char='0', order=-1),
            helpers.fill_str(str(self.transactions), 18, char='0', order=-1),
            helpers.fill_str(str(self.volume), 18, char='0', order=-1), # TODO
            helpers.fill_str(str(self.price_strike) if self.price_strike > 0 else '', 13, char='0'),
            repr(self.price_correction_reference),
            str(self.expiration_date),
            helpers.fill_str(str(self.batch), 7, char='0', order=-1),
            helpers.fill_str(str(self.price_strike_points), 13, char='0'),
            self.isin_id,
            self.dismes
        ])
