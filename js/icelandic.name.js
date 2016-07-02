var options = {
    keys: ['slug'],
    threshold: 1.0
}

var fuzzy_females = new Fuse(names.female, options);
var fuzzy_males = new Fuse(names.male, options);

var my_name = function(name, gender) {
    var icelandic_name = undefined;
    if (gender === 'male') { icelandic_name = fuzzy_males.search(name.unidecode())[0]; }
    else { icelandic_name = fuzzy_females.search(name.unidecode())[0]; }
    return icelandic_name.name;
}

var paternal_name = function(name, gender) {
    var paternal_name = undefined;
    var parent_name = fuzzy_males.search(name.unidecode())[0].genitive;
    if (gender === 'male') { return parent_name + 'son'; }
    else { return parent_name + 'dóttir'; }
}

$('#generate').click(function(event) {
    event.preventDefault();
    var gender = $('input[name="gender"]:checked').val();
    var names = [];
    $.each($('input[name="you"]').val().split(' '), function(index, name) {
	names.push(my_name(name, gender));
    });
    var paternal_first = $('input[name="parental"]').val().split(' ')[0];
    names.push(paternal_name(paternal_first, gender));
    $('#icelandic-name').text(names.join(' '));
});

$(function () {
  $('[data-toggle="popover"]').popover()
})
