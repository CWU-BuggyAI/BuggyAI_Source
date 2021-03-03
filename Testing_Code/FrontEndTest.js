function checkFileType(file) {
    let validExtensions = ['jpg', 'jpeg', 'png'];
    let trimExt = file.name.split('.');
    let extension = trimExt[trimExt.length - 1];

    if (validExtensions.includes(extension.toLowerCase())) {
        console.log('File type valid.')
        return "";
    } else {
        console.log('File type is invalid.')
        return "Invalid file type";
    }
}

function checkFileSize(file) {
    console.log("Num Bytes:", file.size);
    let limit1MB = 1048576;

    if (file.size <= limit1MB) {
        console.log('File size within limit');
        return "";
    } else {
        console.log('File size larger than 1MB');
        return "File size larger than 1MB";
    }
}

function checkSafeFileName(file) {
    let trimName = file.name.split('.');
    let illegalChars = ['\\', '/', ':', '*', '?', '"', '<', '>', '|'];
    let illegalFileNames = ['aux', 'nul', 'prn', 'con', 'lpt', 'com'];

    if (illegalChars.includes(file.name)) {
        console.log('Filename contains an illegal character');
        return "Filename contains an illegal character";
    } 
    if (file.name[0] == '.') {
        console.log('Filename starts with an illegal character');
        return "Filename starts with an illegal character";
    }
    if (illegalFileNames.includes(trimName[0].toLowerCase())) {
        console.log('Filename is not allowed');
        return "Filename is not allowed";
    }

    return "";
}