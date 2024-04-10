from experimentflow import Factor, FactorType


# Test FactorType
def test_factor_type_has_five_types():
    assert len(FactorType) == 5


def test_factor_type_has_correct_values():
    assert FactorType.CATEGORICAL.value == 1
    assert FactorType.NUMERIC.value == 2
    assert FactorType.ORDINAL.value == 3
    assert FactorType.BOOLEAN.value == 4
    assert FactorType.TEXT.value == 5


# Test Factor class attribute name
def test_factor_name_should_be_a_string():
    try:
        Factor(
            name=1,
            description="factor description",
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
        Factor(
            name=True,
            description="factor description",
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
    except ValueError as e:
        assert str(e) == "Factor name should be a string"


def test_factor_name_should_not_be_empty():
    try:
        Factor(
            name="",
            description="factor description",
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
    except ValueError as e:
        assert str(e) == "Factor name should not be empty"


# Test Factor class attribute
def test_factor_description_should_be_a_string():
    try:
        Factor(
            name="factor name",
            description=1,
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
        Factor(
            name="factor name",
            description=True,
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
    except ValueError as e:
        assert str(e) == "Factor description should be a string"


def test_factor_description_should_not_be_empty():
    try:
        Factor(
            name="factor name",
            description="",
            type=FactorType.TEXT,
            values=["text1", "text2"],
        )
    except ValueError as e:
        assert str(e) == "Factor description should not be empty"


# Test Factor class attribute type
def test_factor_type_should_be_a_factor_type():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=1,
            values=["text1", "text2"],
        )
        Factor(
            name="factor name",
            description="factor description",
            type=True,
            values=["text1", "text2"],
        )
    except ValueError as e:
        assert str(e) == "Factor type should be a FactorType"


# Test Factor class attribute values
def test_factor_values_should_be_a_list_or_tuple():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.TEXT,
            values="text1",
        )
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.TEXT,
            values=1,
        )
    except ValueError as e:
        assert str(e) == "Factor values should be a list or tuple"


def test_factor_values_should_not_be_empty():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.TEXT,
            values=[],
        )
    except ValueError as e:
        assert str(e) == "Factor values should not be empty"


def test_factor_values_should_not_contain_duplicate_values():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.TEXT,
            values=["text1", "text1"],
        )
    except ValueError as e:
        assert str(e) == "Factor values should not contain duplicate values"


def test_create_factor_with_a_list_of_values():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.TEXT,
        values=["text1", "text2"],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.TEXT
    assert factor.values == ["text1", "text2"]


def test_create_factor_with_a_tuple_of_values():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.TEXT,
        values=("text1", "text2"),
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.TEXT
    assert factor.values == ("text1", "text2")


def test_all_values_in_a_categorical_factor_should_be_strings():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.CATEGORICAL,
        values=["text1", "text2"],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.CATEGORICAL
    assert factor.values == ["text1", "text2"]


def test_should_raise_error_if_values_in_a_categorical_factor_are_not_strings():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.CATEGORICAL,
            values=[1, "B"],
        )
    except ValueError as e:
        assert str(e) == "Factor values should be strings"


def test_all_values_in_a_numeric_factor_should_be_numbers():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.NUMERIC,
        values=[1, 2],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.NUMERIC
    assert factor.values == [1, 2]


def test_should_raise_error_if_values_in_a_numeric_factor_are_not_numbers():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.NUMERIC,
            values=["A", 2],
        )
    except ValueError as e:
        assert str(e) == "Factor values should be numbers"


def test_all_values_in_an_ordinal_factor_should_be_strings():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.ORDINAL,
        values=["text1", "text2"],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.ORDINAL
    assert factor.values == ["text1", "text2"]


def test_should_raise_error_if_values_in_an_ordinal_factor_are_not_strings():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.ORDINAL,
            values=[1, "B"],
        )
    except ValueError as e:
        assert str(e) == "Factor values should be strings"


def test_boolean_factor_should_have_only_two_values():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.BOOLEAN,
        values=[True, False],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.BOOLEAN
    assert factor.values == [True, False]


def test_should_raise_error_if_boolean_factor_has_more_than_two_values():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.BOOLEAN,
            values=[True, False, "das"],
        )
    except ValueError as e:
        assert str(e) == "Factor values should be booleans"


def test_should_raise_error_if_boolean_factor_has_less_than_two_values():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.BOOLEAN,
            values=[True],
        )
    except ValueError as e:
        assert str(e) == "Boolean factor should have exactly two values (True, False)"


def test_all_values_in_a_text_factor_should_be_strings():
    factor = Factor(
        name="factor name",
        description="factor description",
        type=FactorType.TEXT,
        values=["text1", "text2"],
    )
    assert factor is not None
    assert factor.name == "factor name"
    assert factor.description == "factor description"
    assert factor.type == FactorType.TEXT
    assert factor.values == ["text1", "text2"]


def test_should_raise_error_if_values_in_a_text_factor_are_not_strings():
    try:
        Factor(
            name="factor name",
            description="factor description",
            type=FactorType.TEXT,
            values=[1, "B"],
        )
    except ValueError as e:
        assert str(e) == "Factor values should be strings"
