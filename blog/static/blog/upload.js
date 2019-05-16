document.addEventListener('DOMContentLoaded', e => {
    for (const textarea of document.querySelectorAll('textarea.uploadable')) {
        textarea.addEventListener('dragover', e => {
            e.preventDefault();
        });

        textarea.addEventListener('drop', e => {
            e.preventDefault();
            const formData = new FormData();
            formData.append('file', e.dataTransfer.files[0]);
            fetch('/upload/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': csrftoken,
                },
            }).then(response => {
                return response.json();
            }).then(response => {
                textarea.value += response.url;
            }).catch(error => {
                console.log(error);
            });

        });
    }
});

