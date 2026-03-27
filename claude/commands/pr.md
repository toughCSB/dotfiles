현재 브랜치의 변경 사항으로 Pull Request를 생성합니다.

## 실행 절차

1. 현재 브랜치와 base 브랜치 확인
2. `git log [base]..[current] --oneline` 로 커밋 목록 파악
3. `git diff [base]..[current] --stat` 로 변경 파일 확인
4. PR 제목 및 본문 작성 (한국어)
5. `gh pr create` 로 실제 생성

## PR 본문 형식

```markdown
## 변경 요약
- ...

## 변경 이유
- ...

## 테스트 방법
- [ ] ...

## 체크리스트
- [ ] 테스트 통과
- [ ] 타입 에러 없음
- [ ] 불필요한 console.log 제거
```

## 규칙
- base 브랜치 기본값: `main` (없으면 `master`)
- 민감한 정보(토큰, 비밀번호)가 포함된 커밋 있으면 경고
- draft PR은 `$ARGUMENTS` 에 `draft` 입력 시 생성
