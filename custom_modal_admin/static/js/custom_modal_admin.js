$(function () {
    $('.js-django-admin-custom-modal').each(function (index, element) {
        var $currentEl = $(element);
        $currentEl.on('click', function (e) {
            var targetModalSelector = '[data-django-admin-custom-modal=' + $currentEl.data('targetName') + ']';
            var $targetModal = $(targetModalSelector);
    
            e.preventDefault();
            e.stopPropagation();
            $targetModal.dialog({
            resizable: false,
            height: 'auto',
            width: 'auto',
            modal: true
            });
        });
    });
});
