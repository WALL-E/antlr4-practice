# Generated from MySqlParser.g4 by ANTLR 4.7.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by MySqlParser.

class MySqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySqlParser#root.
    def visitRoot(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlStatements.
    def visitSqlStatements(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlStatement.
    def visitSqlStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#emptyStatement.
    def visitEmptyStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ddlStatement.
    def visitDdlStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dmlStatement.
    def visitDmlStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionStatement.
    def visitTransactionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#replicationStatement.
    def visitReplicationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#preparedStatement.
    def visitPreparedStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#compoundStatement.
    def visitCompoundStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#administrationStatement.
    def visitAdministrationStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#utilityStatement.
    def visitUtilityStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDatabase.
    def visitCreateDatabase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createEvent.
    def visitCreateEvent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createIndex.
    def visitCreateIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createProcedure.
    def visitCreateProcedure(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createFunction.
    def visitCreateFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createServer.
    def visitCreateServer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#copyCreateTable.
    def visitCopyCreateTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryCreateTable.
    def visitQueryCreateTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnCreateTable.
    def visitColumnCreateTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTablespaceInnodb.
    def visitCreateTablespaceInnodb(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTablespaceNdb.
    def visitCreateTablespaceNdb(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTrigger.
    def visitCreateTrigger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createView.
    def visitCreateView(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ownerStatement.
    def visitOwnerStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#preciseSchedule.
    def visitPreciseSchedule(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalSchedule.
    def visitIntervalSchedule(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#timestampValue.
    def visitTimestampValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalExpr.
    def visitIntervalExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalType.
    def visitIntervalType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#enableType.
    def visitEnableType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexType.
    def visitIndexType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexOption.
    def visitIndexOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#procedureParameter.
    def visitProcedureParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionParameter.
    def visitFunctionParameter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineComment.
    def visitRoutineComment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineLanguage.
    def visitRoutineLanguage(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineBehavior.
    def visitRoutineBehavior(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineData.
    def visitRoutineData(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineSecurity.
    def visitRoutineSecurity(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#serverOption.
    def visitServerOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDefinitions.
    def visitCreateDefinitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnDeclaration.
    def visitColumnDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constraintDeclaration.
    def visitConstraintDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexDeclaration.
    def visitIndexDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnDefinition.
    def visitColumnDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nullColumnConstraint.
    def visitNullColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultColumnConstraint.
    def visitDefaultColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#autoIncrementColumnConstraint.
    def visitAutoIncrementColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#primaryKeyColumnConstraint.
    def visitPrimaryKeyColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uniqueKeyColumnConstraint.
    def visitUniqueKeyColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#commentColumnConstraint.
    def visitCommentColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#formatColumnConstraint.
    def visitFormatColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#storageColumnConstraint.
    def visitStorageColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceColumnConstraint.
    def visitReferenceColumnConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#primaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uniqueKeyTableConstraint.
    def visitUniqueKeyTableConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#foreignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTableConstraint.
    def visitCheckTableConstraint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceDefinition.
    def visitReferenceDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceAction.
    def visitReferenceAction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceControlType.
    def visitReferenceControlType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleIndexDeclaration.
    def visitSimpleIndexDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#specialIndexDeclaration.
    def visitSpecialIndexDeclaration(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionEngine.
    def visitTableOptionEngine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionAutoIncrement.
    def visitTableOptionAutoIncrement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionAverage.
    def visitTableOptionAverage(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCharset.
    def visitTableOptionCharset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionChecksum.
    def visitTableOptionChecksum(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCollate.
    def visitTableOptionCollate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionComment.
    def visitTableOptionComment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCompression.
    def visitTableOptionCompression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionConnection.
    def visitTableOptionConnection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionDataDirectory.
    def visitTableOptionDataDirectory(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionDelay.
    def visitTableOptionDelay(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionEncryption.
    def visitTableOptionEncryption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionIndexDirectory.
    def visitTableOptionIndexDirectory(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionInsertMethod.
    def visitTableOptionInsertMethod(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionKeyBlockSize.
    def visitTableOptionKeyBlockSize(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionMaxRows.
    def visitTableOptionMaxRows(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionMinRows.
    def visitTableOptionMinRows(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPackKeys.
    def visitTableOptionPackKeys(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPassword.
    def visitTableOptionPassword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionRowFormat.
    def visitTableOptionRowFormat(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionRecalculation.
    def visitTableOptionRecalculation(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPersistent.
    def visitTableOptionPersistent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionSamplePage.
    def visitTableOptionSamplePage(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionTablespace.
    def visitTableOptionTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionUnion.
    def visitTableOptionUnion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tablespaceStorage.
    def visitTablespaceStorage(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionHash.
    def visitPartitionFunctionHash(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionKey.
    def visitPartitionFunctionKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionRange.
    def visitPartitionFunctionRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionList.
    def visitPartitionFunctionList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subPartitionFunctionHash.
    def visitSubPartitionFunctionHash(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subPartitionFunctionKey.
    def visitSubPartitionFunctionKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionComparision.
    def visitPartitionComparision(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionListAtom.
    def visitPartitionListAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionListVector.
    def visitPartitionListVector(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionSimple.
    def visitPartitionSimple(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinerAtom.
    def visitPartitionDefinerAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinerVector.
    def visitPartitionDefinerVector(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionEngine.
    def visitPartitionOptionEngine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionComment.
    def visitPartitionOptionComment(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionDataDirectory.
    def visitPartitionOptionDataDirectory(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionIndexDirectory.
    def visitPartitionOptionIndexDirectory(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionMaxRows.
    def visitPartitionOptionMaxRows(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionMinRows.
    def visitPartitionOptionMinRows(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionTablespace.
    def visitPartitionOptionTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionNodeGroup.
    def visitPartitionOptionNodeGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterSimpleDatabase.
    def visitAlterSimpleDatabase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUpgradeName.
    def visitAlterUpgradeName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterEvent.
    def visitAlterEvent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterFunction.
    def visitAlterFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterInstance.
    def visitAlterInstance(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterProcedure.
    def visitAlterProcedure(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterServer.
    def visitAlterServer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterTable.
    def visitAlterTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterTablespace.
    def visitAlterTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterView.
    def visitAlterView(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByTableOption.
    def visitAlterByTableOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddColumn.
    def visitAlterByAddColumn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddColumns.
    def visitAlterByAddColumns(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddIndex.
    def visitAlterByAddIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddPrimaryKey.
    def visitAlterByAddPrimaryKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddUniqueKey.
    def visitAlterByAddUniqueKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddSpecialIndex.
    def visitAlterByAddSpecialIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddForeignKey.
    def visitAlterByAddForeignKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterBySetAlgorithm.
    def visitAlterBySetAlgorithm(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByChangeDefault.
    def visitAlterByChangeDefault(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByChangeColumn.
    def visitAlterByChangeColumn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByLock.
    def visitAlterByLock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByModifyColumn.
    def visitAlterByModifyColumn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropColumn.
    def visitAlterByDropColumn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropPrimaryKey.
    def visitAlterByDropPrimaryKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropIndex.
    def visitAlterByDropIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropForeignKey.
    def visitAlterByDropForeignKey(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDisableKeys.
    def visitAlterByDisableKeys(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByEnableKeys.
    def visitAlterByEnableKeys(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRename.
    def visitAlterByRename(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByOrder.
    def visitAlterByOrder(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByConvertCharset.
    def visitAlterByConvertCharset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDefaultCharset.
    def visitAlterByDefaultCharset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDiscardTablespace.
    def visitAlterByDiscardTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByImportTablespace.
    def visitAlterByImportTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByForce.
    def visitAlterByForce(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByValidate.
    def visitAlterByValidate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddPartition.
    def visitAlterByAddPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropPartition.
    def visitAlterByDropPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDiscardPartition.
    def visitAlterByDiscardPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByImportPartition.
    def visitAlterByImportPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByTruncatePartition.
    def visitAlterByTruncatePartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByCoalescePartition.
    def visitAlterByCoalescePartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByReorganizePartition.
    def visitAlterByReorganizePartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByExchangePartition.
    def visitAlterByExchangePartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAnalyzePartitiion.
    def visitAlterByAnalyzePartitiion(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByCheckPartition.
    def visitAlterByCheckPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByOptimizePartition.
    def visitAlterByOptimizePartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRebuildPartition.
    def visitAlterByRebuildPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRepairPartition.
    def visitAlterByRepairPartition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRemovePartitioning.
    def visitAlterByRemovePartitioning(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByUpgradePartitioning.
    def visitAlterByUpgradePartitioning(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropDatabase.
    def visitDropDatabase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropEvent.
    def visitDropEvent(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropIndex.
    def visitDropIndex(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropProcedure.
    def visitDropProcedure(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropFunction.
    def visitDropFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropServer.
    def visitDropServer(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTable.
    def visitDropTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTablespace.
    def visitDropTablespace(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTrigger.
    def visitDropTrigger(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropView.
    def visitDropView(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameTable.
    def visitRenameTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameTableClause.
    def visitRenameTableClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#truncateTable.
    def visitTruncateTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#callStatement.
    def visitCallStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#deleteStatement.
    def visitDeleteStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doStatement.
    def visitDoStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerStatement.
    def visitHandlerStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#insertStatement.
    def visitInsertStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadDataStatement.
    def visitLoadDataStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadXmlStatement.
    def visitLoadXmlStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#replaceStatement.
    def visitReplaceStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleSelect.
    def visitSimpleSelect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionSelect.
    def visitUnionSelect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionParenthesisSelect.
    def visitUnionParenthesisSelect(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#updateStatement.
    def visitUpdateStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#updatedElement.
    def visitUpdatedElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#assignmentField.
    def visitAssignmentField(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockClause.
    def visitLockClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#singleDeleteStatement.
    def visitSingleDeleteStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#multipleDeleteStatement.
    def visitMultipleDeleteStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerOpenStatement.
    def visitHandlerOpenStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerReadIndexStatement.
    def visitHandlerReadIndexStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerReadStatement.
    def visitHandlerReadStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerCloseStatement.
    def visitHandlerCloseStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#singleUpdateStatement.
    def visitSingleUpdateStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#multipleUpdateStatement.
    def visitMultipleUpdateStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByClause.
    def visitOrderByClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByExpression.
    def visitOrderByExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSources.
    def visitTableSources(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceBase.
    def visitTableSourceBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceNested.
    def visitTableSourceNested(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#atomTableItem.
    def visitAtomTableItem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexHint.
    def visitIndexHint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexHintType.
    def visitIndexHintType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#innerJoin.
    def visitInnerJoin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#straightJoin.
    def visitStraightJoin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#outerJoin.
    def visitOuterJoin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#naturalJoin.
    def visitNaturalJoin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryExpression.
    def visitQueryExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryExpressionNointo.
    def visitQueryExpressionNointo(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#querySpecification.
    def visitQuerySpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#querySpecificationNointo.
    def visitQuerySpecificationNointo(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionParenthesis.
    def visitUnionParenthesis(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionStatement.
    def visitUnionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectSpec.
    def visitSelectSpec(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectElements.
    def visitSelectElements(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectStarElement.
    def visitSelectStarElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoVariables.
    def visitSelectIntoVariables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoDumpFile.
    def visitSelectIntoDumpFile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoTextFile.
    def visitSelectIntoTextFile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectFieldsInto.
    def visitSelectFieldsInto(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectLinesInto.
    def visitSelectLinesInto(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fromClause.
    def visitFromClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#groupByItem.
    def visitGroupByItem(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#limitClause.
    def visitLimitClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startTransaction.
    def visitStartTransaction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#beginWork.
    def visitBeginWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#commitWork.
    def visitCommitWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rollbackWork.
    def visitRollbackWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#savepointStatement.
    def visitSavepointStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rollbackStatement.
    def visitRollbackStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#releaseStatement.
    def visitReleaseStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockTables.
    def visitLockTables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unlockTables.
    def visitUnlockTables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setAutocommitStatement.
    def visitSetAutocommitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setTransactionStatement.
    def visitSetTransactionStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionMode.
    def visitTransactionMode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockTableElement.
    def visitLockTableElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockAction.
    def visitLockAction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionOption.
    def visitTransactionOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionLevel.
    def visitTransactionLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#changeMaster.
    def visitChangeMaster(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#changeReplicationFilter.
    def visitChangeReplicationFilter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#purgeBinaryLogs.
    def visitPurgeBinaryLogs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetMaster.
    def visitResetMaster(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetSlave.
    def visitResetSlave(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startSlave.
    def visitStartSlave(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stopSlave.
    def visitStopSlave(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startGroupReplication.
    def visitStartGroupReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stopGroupReplication.
    def visitStopGroupReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterStringOption.
    def visitMasterStringOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterDecimalOption.
    def visitMasterDecimalOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterBoolOption.
    def visitMasterBoolOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterRealOption.
    def visitMasterRealOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterUidListOption.
    def visitMasterUidListOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringMasterOption.
    def visitStringMasterOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#decimalMasterOption.
    def visitDecimalMasterOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#boolMasterOption.
    def visitBoolMasterOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#channelOption.
    def visitChannelOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doDbReplication.
    def visitDoDbReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ignoreDbReplication.
    def visitIgnoreDbReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doTableReplication.
    def visitDoTableReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ignoreTableReplication.
    def visitIgnoreTableReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#wildDoTableReplication.
    def visitWildDoTableReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#wildIgnoreTableReplication.
    def visitWildIgnoreTableReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rewriteDbReplication.
    def visitRewriteDbReplication(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tablePair.
    def visitTablePair(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#threadType.
    def visitThreadType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#gtidsUntilOption.
    def visitGtidsUntilOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterLogUntilOption.
    def visitMasterLogUntilOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#relayLogUntilOption.
    def visitRelayLogUntilOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlGapsUntilOption.
    def visitSqlGapsUntilOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userConnectionOption.
    def visitUserConnectionOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordConnectionOption.
    def visitPasswordConnectionOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultAuthConnectionOption.
    def visitDefaultAuthConnectionOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#pluginDirConnectionOption.
    def visitPluginDirConnectionOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#gtuidSet.
    def visitGtuidSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaStartTransaction.
    def visitXaStartTransaction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaEndTransaction.
    def visitXaEndTransaction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaPrepareStatement.
    def visitXaPrepareStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaCommitWork.
    def visitXaCommitWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaRollbackWork.
    def visitXaRollbackWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaRecoverWork.
    def visitXaRecoverWork(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#prepareStatement.
    def visitPrepareStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#executeStatement.
    def visitExecuteStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#deallocatePrepare.
    def visitDeallocatePrepare(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineBody.
    def visitRoutineBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#blockStatement.
    def visitBlockStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseStatement.
    def visitCaseStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifStatement.
    def visitIfStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#iterateStatement.
    def visitIterateStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#leaveStatement.
    def visitLeaveStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loopStatement.
    def visitLoopStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#repeatStatement.
    def visitRepeatStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#returnStatement.
    def visitReturnStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#whileStatement.
    def visitWhileStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#CloseCursor.
    def visitCloseCursor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#FetchCursor.
    def visitFetchCursor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#OpenCursor.
    def visitOpenCursor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareVariable.
    def visitDeclareVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareCondition.
    def visitDeclareCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareCursor.
    def visitDeclareCursor(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareHandler.
    def visitDeclareHandler(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionCode.
    def visitHandlerConditionCode(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionState.
    def visitHandlerConditionState(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionName.
    def visitHandlerConditionName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionWarning.
    def visitHandlerConditionWarning(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionNotfound.
    def visitHandlerConditionNotfound(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionException.
    def visitHandlerConditionException(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#procedureSqlStatement.
    def visitProcedureSqlStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseAlternative.
    def visitCaseAlternative(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#elifAlternative.
    def visitElifAlternative(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUserMysqlV56.
    def visitAlterUserMysqlV56(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUserMysqlV57.
    def visitAlterUserMysqlV57(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUserMysqlV56.
    def visitCreateUserMysqlV56(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUserMysqlV57.
    def visitCreateUserMysqlV57(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropUser.
    def visitDropUser(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#grantStatement.
    def visitGrantStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#grantProxy.
    def visitGrantProxy(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameUser.
    def visitRenameUser(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#detailRevoke.
    def visitDetailRevoke(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#shortRevoke.
    def visitShortRevoke(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#revokeProxy.
    def visitRevokeProxy(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setPasswordStatement.
    def visitSetPasswordStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userSpecification.
    def visitUserSpecification(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordAuthOption.
    def visitPasswordAuthOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringAuthOption.
    def visitStringAuthOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#hashAuthOption.
    def visitHashAuthOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleAuthOption.
    def visitSimpleAuthOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tlsOption.
    def visitTlsOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userResourceOption.
    def visitUserResourceOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userPasswordOption.
    def visitUserPasswordOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userLockOption.
    def visitUserLockOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privelegeClause.
    def visitPrivelegeClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privilege.
    def visitPrivilege(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#currentSchemaPriviLevel.
    def visitCurrentSchemaPriviLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#globalPrivLevel.
    def visitGlobalPrivLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteSchemaPrivLevel.
    def visitDefiniteSchemaPrivLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteFullTablePrivLevel.
    def visitDefiniteFullTablePrivLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteTablePrivLevel.
    def visitDefiniteTablePrivLevel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameUserClause.
    def visitRenameUserClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#analyzeTable.
    def visitAnalyzeTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTable.
    def visitCheckTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checksumTable.
    def visitChecksumTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#optimizeTable.
    def visitOptimizeTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#repairTable.
    def visitRepairTable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTableOption.
    def visitCheckTableOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUdfunction.
    def visitCreateUdfunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#installPlugin.
    def visitInstallPlugin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uninstallPlugin.
    def visitUninstallPlugin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setVariable.
    def visitSetVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setCharset.
    def visitSetCharset(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setNames.
    def visitSetNames(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setPassword.
    def visitSetPassword(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setTransaction.
    def visitSetTransaction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setAutocommit.
    def visitSetAutocommit(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showMasterLogs.
    def visitShowMasterLogs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showLogEvents.
    def visitShowLogEvents(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showObjectFilter.
    def visitShowObjectFilter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showColumns.
    def visitShowColumns(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateDb.
    def visitShowCreateDb(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateFullIdObject.
    def visitShowCreateFullIdObject(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateUser.
    def visitShowCreateUser(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showEngine.
    def visitShowEngine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGlobalInfo.
    def visitShowGlobalInfo(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showErrors.
    def visitShowErrors(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCountErrors.
    def visitShowCountErrors(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSchemaFilter.
    def visitShowSchemaFilter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showRoutine.
    def visitShowRoutine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGrants.
    def visitShowGrants(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showIndexes.
    def visitShowIndexes(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showOpenTables.
    def visitShowOpenTables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showProfile.
    def visitShowProfile(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSlaveStatus.
    def visitShowSlaveStatus(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#variableClause.
    def visitVariableClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCommonEntity.
    def visitShowCommonEntity(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showFilter.
    def visitShowFilter(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGlobalInfoClause.
    def visitShowGlobalInfoClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSchemaEntity.
    def visitShowSchemaEntity(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showProfileType.
    def visitShowProfileType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binlogStatement.
    def visitBinlogStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#cacheIndexStatement.
    def visitCacheIndexStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#flushStatement.
    def visitFlushStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#killStatement.
    def visitKillStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadIndexIntoCache.
    def visitLoadIndexIntoCache(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetStatement.
    def visitResetStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#shutdownStatement.
    def visitShutdownStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableIndexes.
    def visitTableIndexes(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleFlushOption.
    def visitSimpleFlushOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#channelFlushOption.
    def visitChannelFlushOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableFlushOption.
    def visitTableFlushOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#flushTableOption.
    def visitFlushTableOption(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadedTableIndexes.
    def visitLoadedTableIndexes(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleDescribeStatement.
    def visitSimpleDescribeStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullDescribeStatement.
    def visitFullDescribeStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#helpStatement.
    def visitHelpStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#useStatement.
    def visitUseStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#describeStatements.
    def visitDescribeStatements(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#describeConnection.
    def visitDescribeConnection(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullId.
    def visitFullId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableName.
    def visitTableName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnName.
    def visitFullColumnName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexColumnName.
    def visitIndexColumnName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userName.
    def visitUserName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mysqlVariable.
    def visitMysqlVariable(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charsetName.
    def visitCharsetName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collationName.
    def visitCollationName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#engineName.
    def visitEngineName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uuidSet.
    def visitUuidSet(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xid.
    def visitXid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xuidStringId.
    def visitXuidStringId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#authPlugin.
    def visitAuthPlugin(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uid.
    def visitUid(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleId.
    def visitSimpleId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dottedId.
    def visitDottedId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fileSizeLiteral.
    def visitFileSizeLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringLiteral.
    def visitStringLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nullNotnull.
    def visitNullNotnull(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constant.
    def visitConstant(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringDataType.
    def visitStringDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dimensionDataType.
    def visitDimensionDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleDataType.
    def visitSimpleDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collectionDataType.
    def visitCollectionDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#spatialDataType.
    def visitSpatialDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#convertedDataType.
    def visitConvertedDataType(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthOneDimension.
    def visitLengthOneDimension(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthTwoDimension.
    def visitLengthTwoDimension(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthTwoOptionalDimension.
    def visitLengthTwoOptionalDimension(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uidList.
    def visitUidList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tables.
    def visitTables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexColumnNames.
    def visitIndexColumnNames(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressions.
    def visitExpressions(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionsWithDefaults.
    def visitExpressionsWithDefaults(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constants.
    def visitConstants(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleStrings.
    def visitSimpleStrings(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userVariables.
    def visitUserVariables(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultValue.
    def visitDefaultValue(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#currentTimestamp.
    def visitCurrentTimestamp(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifExists.
    def visitIfExists(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifNotExists.
    def visitIfNotExists(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordFunctionCall.
    def visitPasswordFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelWeightList.
    def visitLevelWeightList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelWeightRange.
    def visitLevelWeightRange(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelInWeightListElement.
    def visitLevelInWeightListElement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordFunctionClause.
    def visitPasswordFunctionClause(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArgs.
    def visitFunctionArgs(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArg.
    def visitFunctionArg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isExpression.
    def visitIsExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#notExpression.
    def visitNotExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalExpression.
    def visitLogicalExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#inPredicate.
    def visitInPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryComparasionPredicate.
    def visitSubqueryComparasionPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binaryComparasionPredicate.
    def visitBinaryComparasionPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#likePredicate.
    def visitLikePredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collateExpressionAtom.
    def visitCollateExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryExpessionAtom.
    def visitSubqueryExpessionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mysqlVariableExpressionAtom.
    def visitMysqlVariableExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nestedRowExpressionAtom.
    def visitNestedRowExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#existsExpessionAtom.
    def visitExistsExpessionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryOperator.
    def visitUnaryOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#bitOperator.
    def visitBitOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathOperator.
    def visitMathOperator(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charsetNameBase.
    def visitCharsetNameBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionLevelBase.
    def visitTransactionLevelBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privilegesBase.
    def visitPrivilegesBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dataTypeBase.
    def visitDataTypeBase(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionNameBase.
    def visitFunctionNameBase(self, ctx):
        return self.visitChildren(ctx)


