var h = maquette.h;
var projector = maquette.createProjector();

var state = {
    files: [
        {
            "id": 1,
            "name": "file1",
            "type": "file",
            "path": "/dummy/path/"
        },
        {
            "id": 2,
            "name": "long directory name",
            "type": "dir",
            "path": "/dummy/path2/"
        }

    ],
    upload_form_display: "none",
}

function l(message) {
    console.log(message);
}

var gaccount = {
    render: function() {
        return (
            h("a.account", {href: "#"}, [
                h("img", {src: "./img/icons/SVG/account.svg"})
            ])
        );
    }
}

var gsearch_input = {
    render: function() {
        return (
            h("input.form-ctrl", {placeholder: "search files and folders..."})
        );
    }
}

var gsearch_box = {
    render: function() {
        return (
            h("span.search-box", [
                gsearch_input.render(),
                h("img.search", {src: "./img/icons/SVG/search.svg"}),
            ])
        );
    }
}

var glogo = {
    render: function() {
        return (
            h("a.btn.logo", [ 
                h("img.logo", {src: "./img/icons/SVG/logo.svg"}),
                h("span.logo-text", ["Pandora"])
             ])
        );
    }
}

var gmenu_button = {
    render: function() {
        return (
            h("a.btn.menu-btn", [ 
                h("img", {src: "./img/icons/SVG/menu.svg"})
             ])
        );
    }
}

var header = {
    render: function() {
        return (
            h("header.navbar", [
                gmenu_button.render(),
                glogo.render(),
                gsearch_box.render(),
                gaccount.render(),
            ])
        );
    }
}

var label = {
    render: function() {
        return (
            h("h1.main-label", ["Home"])
        );
    }
}

function uploadFile(e) {
    e.preventDefault();
    let file = document.querySelector("#upload-file").value;
    let fname = document.querySelector("#upload-name").value;
    
}

var upload_form = {
    render: function() {
        return (
            h("div.modal", {style: "display:" + window.state.upload_form_display + ";"}, [
                h("form#upload", {onsubmit: uploadFile}, [
                    cross.render({modal: upload_form}),
                    h("h3.title", ["Upload File"]),
                    h("input.form-ctrl", {placeholder: "name...", id: "upload-name"}),
                    h("input", {type: "file", id: "upload-file"}),
                    h("button", {type: "submit"}, ["upload"])
                ])
            ])
        );
    }
}

function dismiss_upload_modal() {
    window.state.upload_form_display = "none";
    projector.scheduleRender(); 
}

var cross = {
    render: function(props) {
        return (
            h("a.cross", {onclick: dismiss_upload_modal}, [
                h("img", {src: "/img/icons/SVG/cross.svg"})
            ])
        );
    }
}

function display_upload_modal() {
    let app = document.querySelector("#app");
    window.state.upload_form_display = "flex";
    projector.append(app, upload_form.render);
}

var upload = {
    render: function() {
        return (
            h("a.upload-btn", {onclick: display_upload_modal}, [
                h("img", {src: "/img/icons/SVG/upload.svg"})
            ])
        );
    }
}

var create_folder = {
    render: function() {
        return (
            h("a.create-folder-btn", [
                h("img", {src: "/img/icons/SVG/create_folder.svg"})
            ])
        );
    }
}

var delete_btn = {
    render: function() {
        return (
            h("a.delete-btn", [
                h("img", {src: "/img/icons/SVG/delete.svg"})
            ])
        );
    }
}

var toolbar = {
    render: function() {
        return (
            h("div.toolbar", [
                upload.render(),
                create_folder.render(),
                delete_btn.render()
            ])
        );
    }
}

var file = {
    render: function(props) {
        type = props.type == "file" ? "file" : "dir";
        return (
            h("div.file", [
                h("img." + type, {src: "/img/icons/SVG/" + type + ".svg"}),
                h("span.name", [props.name])
            ])
        );
    }
}

var library = {
    render: function() {
        return (
            h("div.library", [
                file.render(window.state.files[0]),
                file.render(window.state.files[1])
            ])
        );
    }
}

var body = {
    render: function() {
        return (
            h("div.body", [
                label.render(),
                toolbar.render(),
                library.render()
            ])
        );
    }
}

var App = {
    render: function() {
        return (
            h("section.body", [
                header.render(), 
                body.render()
            ])
        );
    }
}

document.addEventListener("DOMContentLoaded", function() {
    let app = document.querySelector("#app");
    projector.append(app, App.render);
});