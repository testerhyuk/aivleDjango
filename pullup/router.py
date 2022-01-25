class DBRouter:
    # pullup 앱에서 수행되는 모든 데이터베이스 연산을 제어할 수 있다.
    def db_for_read(self, model, **hints):
        # pullup 앱의 모델을 조회하는 경우 custom으로 중계한다.
        if model._meta.app_label == 'pullup':
            return 'custom'
        return None
        
    def db_for_write(self, model, **hints):
        # pullup 앱의 모델을 기록하는 경우 custom으로 중계한다.
        if model._meta.app_label == 'pullup':
            return 'custom'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        # pullup 앱의 모델과 관련된 관계 접근 허용
        if obj1._meta.app_label == 'pullup' or \
        obj2._meta.app_label == 'pullup':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        # pullup 앱의 모델에 대응하는 표가 custom 데이터베이스에만 생성되도록 한다.
        if app_label == 'pullup':
            return db == 'custom'
        return None