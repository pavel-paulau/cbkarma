function (doc) {
    if (doc.type === 'update') {
        emit(doc._id, null);
    }
}
