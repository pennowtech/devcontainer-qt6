#include <QGuiApplication>
#include <QQmlApplicationEngine>

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv);

    const auto applicationDirPath = QCoreApplication::applicationDirPath();
    QQmlApplicationEngine engine;
    engine.addImportPath(QString("%1/qml/").arg(applicationDirPath));
    engine.addImportPath("qrc:/");

    engine.load(QUrl::fromLocalFile(QString("%1/qml/main.qml").arg(applicationDirPath)));
    if (engine.rootObjects().isEmpty()) {
        // LOG_ERROR(appLogger, "Failed to load QML root objects");
        return -1;
    }

    return app.exec();
}
